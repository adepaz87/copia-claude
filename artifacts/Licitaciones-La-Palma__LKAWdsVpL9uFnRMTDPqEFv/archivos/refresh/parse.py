"""Extract La Palma tenders from PLACSP ATOM feeds (zip archives or .atom files).
Usage: python3 parse.py out.json input1 [input2 ...]
Later inputs/entries with newer <updated> win per tender id."""
import sys, re, json, zipfile, html

PALMA_NAMES = re.compile(r"(de\s+La\s+Palma(?!\s+del\s+Condado|\s+d.Ebre)|Llanos\s+de\s+Aridane|Tazacorte|Bre[ñn]a\s+(Alta|Baja)|Villa\s+de\s+Mazo|Fuencaliente|Tijarafe|Puntagorda|Garaf[ií]a|Barlovento|San\s+Andr[eé]s\s+y\s+Sauces|Puntallana|(?-i:El\s+Paso)\b)", re.I)
STATUS = {"PRE": "Anuncio previo", "PUB": "En plazo", "EV": "Pendiente de adjudicación", "ADJ": "Adjudicada", "RES": "Resuelta", "ANUL": "Anulada"}
TYPE = {"1": "Suministros", "2": "Servicios", "3": "Obras", "21": "Gestión de servicios públicos", "22": "Concesión de servicios", "31": "Concesión de obras", "32": "Concesión de obras", "40": "Colaboración público-privada", "7": "Administrativo especial", "8": "Privado", "50": "Patrimonial"}
PROC = {"1": "Abierto", "2": "Restringido", "3": "Negociado sin publicidad", "4": "Negociado con publicidad", "5": "Diálogo competitivo", "6": "Contrato menor", "7": "Derivado de acuerdo marco", "8": "Concurso de proyectos", "9": "Abierto simplificado", "10": "Asociación para la innovación", "11": "Derivado de asociación para la innovación", "12": "Sistema dinámico de adquisición", "13": "Licitación con negociación", "100": "Normas internas", "999": "Otros"}

def t(rx, s, flags=re.S):
    m = re.search(rx, s, flags)
    return html.unescape(m.group(1).strip()) if m else None

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

REGIONAL = re.compile(r"Comunidad Aut[oó]noma de Canarias|Instituto de Astrof[ií]sica de Canarias|Viviendas Sociales e Infraestructuras de Canarias|VISOCAN|Instituto Canario de la Vivienda|Reserva Mundial de la Biosfera La Palma", re.I)
SCS_CENTRO = re.compile(r"Hospital|Gerencia|Atenci[oó]n Primaria|[AÁ]rea de Salud|Complejo Hospitalario", re.I)

def is_regional(e):
    """Bodies the user follows across Canarias: Gobierno de Canarias (consejerías, DG, organismos),
    IAC, VISOCAN, ICAVI, Reserva de la Biosfera. Hospitals and health-area managements of the
    Servicio Canario de la Salud are left out (those in La Palma come in through is_palma)."""
    party = t(r"<cac-place-ext:LocatedContractingParty>(.*?)</cac-place-ext:LocatedContractingParty>", e) or ""
    names = re.findall(r"<cac:PartyName>\s*<cbc:Name>(.*?)</cbc:Name>", party)
    chain = " > ".join(html.unescape(n) for n in names)
    if not REGIONAL.search(chain): return False
    if "Servicio Canario de la Salud" in chain and SCS_CENTRO.search(names[0] if names else ""): return False
    return True

def is_palma(e):
    loc = t(r"<cac:RealizedLocation>(.*?)</cac:RealizedLocation>", e) or ""
    # ES707 = La Palma, but some bodies mislabel Las Palmas province with it
    if re.search(r"CountrySubentityCode[^>]*>ES707<", loc) and not re.search(r"<cbc:CountrySubentity>\s*Palmas", loc): return True
    if re.search(r"<cbc:PostalZone>387\d\d<", loc): return True
    party = t(r"<cac-place-ext:LocatedContractingParty>(.*?)</cac-place-ext:LocatedContractingParty>", e) or ""
    pz = t(r"<cbc:PostalZone>(.*?)</cbc:PostalZone>", party) or ""
    if pz.startswith("387"): return True
    # name-based match only for bodies located in Santa Cruz de Tenerife province (or without postcode)
    if pz and not pz.startswith("38"): return False
    name = t(r"<cac:PartyName>\s*<cbc:Name>(.*?)</cbc:Name>", party) or ""
    city = t(r"<cbc:CityName>(.*?)</cbc:CityName>", party) or ""
    title = t(r"<title>(.*?)</title>", e) or ""
    return bool(PALMA_NAMES.search(name) or PALMA_NAMES.search(city) or (pz.startswith("38") and PALMA_NAMES.search(title)))

def parse(e, menor_feed=False):
    folder = t(r"<cac-place-ext:ContractFolderStatus>(.*)</cac-place-ext:ContractFolderStatus>", e) or ""
    party = t(r"<cac-place-ext:LocatedContractingParty>(.*?)</cac-place-ext:LocatedContractingParty>", folder) or ""
    proj = t(r"<cac:ProcurementProject>(.*?)</cac:ProcurementProject>", folder) or ""
    proc = t(r"<cac:TenderingProcess>(.*?)</cac:TenderingProcess>", folder) or ""
    st = t(r"ContractFolderStatusCode[^>]*>(.*?)<", folder)
    tc = t(r"<cbc:TypeCode[^>]*>(.*?)<", proj)
    pc = t(r"<cbc:ProcedureCode[^>]*>(.*?)<", proc)
    dl_d = t(r"<cac:TenderSubmissionDeadlinePeriod>.*?<cbc:EndDate>(.*?)</cbc:EndDate>", proc)
    dl_t = t(r"<cac:TenderSubmissionDeadlinePeriod>.*?<cbc:EndTime>(.*?)</cbc:EndTime>", proc)
    winners = list(dict.fromkeys(html.unescape(w) for w in re.findall(r"<cac:WinningParty>.*?<cbc:Name>(.*?)</cbc:Name>", folder, re.S)))
    award = sum(num(a) or 0 for a in re.findall(r"<cac:AwardedTenderedProject>.*?<cbc:TaxExclusiveAmount[^>]*>(.*?)<", folder, re.S)) or None
    pub = re.findall(r"<cbc:IssueDate>(\d{4}-\d\d-\d\d)</cbc:IssueDate>", folder)
    return {
        "id": t(r"<id>(.*?)</id>", e),
        "expediente": t(r"<cbc:ContractFolderID>(.*?)<", folder),
        "titulo": t(r"<title>(.*?)</title>", e),
        "url": t(r'<link href="(.*?)"', e),
        "actualizado": t(r"<updated>(.*?)</updated>", e),
        "estado": STATUS.get(st, st),
        "organo": t(r"<cac:PartyName>\s*<cbc:Name>(.*?)</cbc:Name>", party),
        "municipio": t(r"<cbc:CityName>(.*?)</cbc:CityName>", party),
        "tipo": TYPE.get(tc, tc or "Otros"),
        "procedimiento": PROC.get(pc, pc),
        "importe": num(t(r"<cbc:TaxExclusiveAmount[^>]*>(.*?)<", proj)),
        "valor_estimado": num(t(r"<cbc:EstimatedOverallContractAmount[^>]*>(.*?)<", proj)),
        "cpv": list(dict.fromkeys(re.findall(r"<cbc:ItemClassificationCode[^>]*>(\d+)<", proj))),
        "lugar": t(r"<cac:RealizedLocation>.*?<cbc:CountrySubentity>(.*?)<", proj),
        "plazo": (dl_d + ("T" + dl_t[:5] if dl_t else "")) if dl_d else None,
        "publicado": min(pub) if pub else None,
        "adjudicatario": "; ".join(winners) or None,
        "importe_adjudicacion": award,
        "menor": bool(menor_feed or pc == "6"),
    }

def entries(path):
    if path.endswith(".zip"):
        z = zipfile.ZipFile(path)
        for n in z.namelist():
            if n.endswith(".atom"):
                yield from z.read(n).decode("utf-8", "replace").split("<entry>")[1:]
    else:
        yield from open(path, encoding="utf-8", errors="replace").read().split("<entry>")[1:]

def main():
    out, inputs = sys.argv[1], sys.argv[2:]
    try:
        prev = json.load(open(out))
        prev = prev["licitaciones"] if isinstance(prev, dict) else prev
        data = {d["id"]: d for d in prev}
    except Exception: data = {}
    for p in inputs:
        for e in entries(p):
            palma = is_palma(e)
            if not palma and not is_regional(e): continue
            d = parse(e, "contratosMenores" in p or p.split("/")[-1].startswith("men"))
            d["ambito"] = "La Palma" if palma else "Canarias"
            if not d["id"]: continue
            old = data.get(d["id"])
            if not old or (d["actualizado"] or "") >= (old["actualizado"] or ""):
                data[d["id"]] = d
        print(p, len(data), file=sys.stderr)
    from datetime import datetime, timezone
    rows = sorted(data.values(), key=lambda d: d["actualizado"] or "", reverse=True)
    json.dump({"actualizado": datetime.now(timezone.utc).isoformat(timespec="minutes"), "licitaciones": rows}, open(out, "w"), ensure_ascii=False)

main()
