# Sistema autónomo FV de aviso de parada – Parada de guaguas Ctra. La Grama (Breña Alta)

Cliente: Cabildo de La Palma · Nov 6, 2026 · @Alberto de Paz Bethencourt

## 1. Antecedentes, objeto y alcance

Se propone un sistema aislado de red, alimentado por un generador fotovoltaico de 400 Wp a 24 V cc. Un pulsador en la parada activa una señal luminosa situada unos 270 m antes, en el sentido de llegada de la guagua, para que el conductor sepa que debe parar. El conductor borra el aviso con un mando de radio, tipo puerta de garaje, una vez atendida la parada.

Alcance: generador FV, acumulación, control, pulsador y pilotos en la parada, receptor de radio y mandos, señal luminosa en carretera, y canalización y cableado entre ambos puntos.

| Punto | Situación (UTM 28N REGCAN95, medida en plano) |
| --- | --- |
| Parada de guaguas (marquesina existente de fábrica de bloques con pulsador y pilotos; columna FV de 4 m con armario) | X ≈ 228.995 · Y ≈ 3.174.252 |
| Semáforo de aviso (margen derecho, sentido de llegada) | X ≈ 228.810 · Y ≈ 3.174.058 |
| Recorrido de canalización | 320 m de zanja (plano P-01) |

## 2. Emplazamiento y trazado

La parada está en el margen derecho de la Ctra. de La Grama (LP-3), en Breña Alta, junto a la intersección con la Urbanización La Grama. El semáforo se coloca en el mismo margen, unos 270 m antes, en el sentido de llegada de la guagua (plano P-01).

| Elemento | UTM 28N REGCAN95 | Geográficas (aprox.) |
| --- | --- | --- |
| Marquesina y columna FV | X ≈ 228.995 · Y ≈ 3.174.252 | 28°40'01,6" N · 17°46'22,5" O |
| Semáforo | X ≈ 228.810 · Y ≈ 3.174.058 | 28°39'55,1" N · 17°46'29,4" O |

Las coordenadas se han medido sobre la ortofoto de IDECanarias (escala aprox. 1:1.033) y deben confirmarse en el replanteo.

La marquesina existente es de fábrica de bloques enfoscada y pintada, con cubierta de teja. En ella solo se instalan el pulsador, los pilotos, el zumbador y la placa de instrucciones, fijados con anclaje químico y con el cableado empotrado en roza. Los módulos FV y el armario van en una columna galvanizada propia de 4 m junto a la marquesina, situada de forma que no se den sombra con la farola solar existente.

**Trazado de la canalización.** Sale de la base de la columna FV y baja hacia el suroeste, paralela al margen derecho de la LP-3. Cruza el ramal de la intersección con un tramo hormigonado de unos 20 m y sigue por el margen hasta el semáforo.

| Tramo | Longitud supuesta (m) | Reposición |
| --- | --- | --- |
| Terreno natural / margen | 240 | Restitución del terreno |
| Acera (junto a parada e intersección) | 60 | Solera HM-20 y acabado igual al existente |
| Cruce de calzada | 20 | Firme asfáltico: base, riego y MBC 6 cm |
| **Total zanja** | **320** |  |

El reparto por tipo de superficie es una hipótesis sobre la ortofoto y se ajustará en el replanteo, junto con la detección de servicios existentes.

## 3. Normativa de aplicación

La instalación es de muy baja tensión de seguridad (24 V cc), aislada de red, y se sitúa en el dominio público de una carretera insular. Le aplica, como mínimo:

| Ámbito | Norma |
| --- | --- |
| Electricidad | Reglamento Electrotécnico para Baja Tensión (RD 842/2002) y sus ITC; en especial ITC-BT-36 (muy baja tensión), ITC-BT-21 (tubos) e ITC-BT-40 (instalaciones generadoras aisladas) |
| Carreteras | Ley 9/1991 de Carreteras de Canarias y su Reglamento (Decreto 131/1995): autorización del Cabildo, como titular de la LP-3, para obras en zona de dominio público |
| Tráfico y señalización | Reglamento General de Circulación (RD 1428/2003); UNE-EN 12368 (cabezas de semáforo); Norma 8.1-IC de señalización vertical para la placa complementaria |
| Accesibilidad | Orden TMA/851/2021, condiciones de accesibilidad en espacios públicos urbanizados |
| Equipos | Marcado CE; Directiva 2014/53/UE de equipos radioeléctricos (mandos y receptor); UNE-EN 61215 y UNE-EN 61730 (módulos FV) |
| Obra | RD 1627/1997 (seguridad y salud en obras de construcción); RD 105/2008 (residuos de construcción y demolición) |
| Contratación | Ley 9/2017 de Contratos del Sector Público |

## 4. Funcionamiento

El aviso queda memorizado en un autómata desde que el usuario pulsa hasta que el conductor lo borra con el mando. Si nadie lo borra, un temporizador lo anula automáticamente.

1. **Reposo:** piloto verde "Pulse para solicitar parada" encendido y semáforo en verde fijo.
2. **Solicitud:** el usuario pulsa. Suena un pitido corto de confirmación, se apaga el verde y se enciende el piloto ámbar "Parada solicitada". El semáforo pasa de verde fijo a ámbar intermitente a 1 Hz.
3. Las pulsaciones repetidas se ignoran mientras el aviso está activo (protección antivandálica).
4. La guagua pasa junto a la señal, el conductor ve el aviso y para en la parada.
5. **Reset:** ya parado, el conductor pulsa el mando. Se borra el aviso y el sistema vuelve a reposo. Durante 20 s se bloquea el pulsador, para que una pulsación mantenida no reactive el aviso.
6. **Reset automático:** si no se borra en 90 min (ajustable), el aviso se anula. Así se evitan avisos falsos y gasto inútil de batería.
7. **Batería baja:** el regulador desconecta las cargas (LVD) antes de dañar la batería y las reconecta solo al recargar.

| Estado | Piloto verde | Piloto ámbar | Semáforo en carretera | Sale del estado con |
| --- | --- | --- | --- | --- |
| Reposo | Encendido | Apagado | Verde fijo | Pulsador |
| Aviso activo | Apagado | Encendido | Ámbar intermitente 1 Hz | Mando del conductor, llave de mantenimiento o temporizador 90 min |
| Batería baja (LVD) | Apagado | Apagado | Apagado | Recarga solar |
|  |  |  |  |  |

**Asignación de E/S del autómata (LOGO! 12/24 RCE o equivalente)**

| E/S | Elemento |
| --- | --- |
| I1 | Pulsador de la parada (NA) |
| I2 | Receptor de radio, relé canal 1 (NA, modo impulso) |
| I3 | Llave de mantenimiento: reset y prueba |
| Q1 | Semáforo, foco ámbar (destellos generados por el autómata) |
| Q2 | Piloto ámbar + zumbador de confirmación |
| Q3 | Piloto verde |
| Q4 | Semáforo, foco verde |

Lógica: biestable RS con prioridad al reset. Set = I1 (filtro 0,2 s, bloqueado 20 s tras un reset). Reset = I2 o I3 o retardo a la conexión de 90 min desde el set. Q1 = RS y generador de impulsos 0,5/0,5 s; Q2 = RS; Q3 y Q4 = no RS; zumbador = impulso de 1 s al activarse el set.

## 5. Arquitectura

&#91;embedded content: Esquema de bloques del sistema · parada y señal\]

Toda la energía y el control están en el armario de la parada. Hasta el semáforo solo llega un cable de 4 conductores a 24 V, y el receptor de radio queda en la parada, donde el conductor pulsa el mando ya detenido.

## 6. Balance energético y dimensionado FV

El consumo de diseño es de 240 Wh/día: semáforo en verde fijo en reposo y en ámbar intermitente durante 16 h/día de aviso activo. Se sobredimensiona para el invierno: 400 Wp y una batería LiFePO4 de 25,6 V y 100 Ah, con 8,5 días de autonomía sin sol.

| Carga | Potencia (W) | Horas/día equivalentes | Energía (Wh/día) |
| --- | --- | --- | --- |
| Autómata LOGO! 12/24 RCE | 1,5 | 24 | 36 |
| Receptor de radio 24 V | 0,5 | 24 | 12 |
| Piloto LED 22 mm (siempre hay uno encendido) | 0,5 | 24 | 12 |
| Semáforo, foco ámbar 8 W con destellos al 50 % | 4 | 16 (aviso activo) | 64 |
| Semáforo, foco verde 8 W fijo | 8 | 8 (reposo) | 64 |
| Pérdidas en el cable del semáforo (≈ 3 %) | — | — | 4 |
| **Subtotal** |  |  | **192** |
| **Consumo de diseño** (rendimiento batería + regulador 0,8) |  |  | **240** |

El consumo en espera (autómata, receptor y piloto) supone casi la mitad del total.

**Batería.** LiFePO4 de 25,6 V y 100 Ah con BMS (2.560 Wh). Con una descarga útil del 80 % quedan 2.048 Wh, es decir, 8,5 días a 240 Wh/día. Frente a AGM ofrece más ciclos, menos peso y ningún mantenimiento. El armario debe llevar techo parasol y ventilación para no superar 45 °C en carga.

**Generador FV.** Se toma como mes peor diciembre, con 3,0 HSP (kWh/m²·día) estimadas sobre plano inclinado 50° orientado al sur. Es una estimación conservadora para la vertiente este, afectada por las nubes del alisio; se contrastará con PVGIS en el replanteo.

```latex
P_{FV,min} = \frac{E_d}{HSP \cdot PR} = \frac{240}{3{,}0 \cdot 0{,}75} \approx 107\ \text{Wp}
```

Se instalan 400 Wp, casi 4 veces el mínimo: 2 módulos de 200 Wp en serie (Vmp ≈ 40 V). En diciembre producen unos 900 Wh/día. Con una batería vacía, la recargan en unos 3 días de sol. Aun con solo 1,5 HSP cubren el consumo diario.

**Regulador.** MPPT 100/20 a 24 V con salida de carga, desconexión por baja tensión (LVD) y Bluetooth para revisar el histórico desde el móvil (p. ej. Victron SmartSolar 100/20). La corriente de carga máxima es 400 W / 25,6 V = 15,6 A, por debajo de los 20 A del equipo.

Inclinación 50° al sur, sin sombras de arbolado, talud ni de la propia marquesina. Los módulos van en una columna galvanizada propia de 4 m, a la que también se fija el armario, fuera del alcance de la mano.

## 7. Canalización, cableado y caída de tensión

El semáforo se alimenta desde el armario de la parada con cable RV-K 0,6/1 kV de 4×6 mm² (común, ámbar, verde y reserva). La caída de tensión en los 350 m es del 2,9 %. Todo el sistema trabaja a 24 V cc, en muy baja tensión de seguridad (MBTS, ITC-BT-36).

Longitud: la zanja tiene 320 m y el cable 350 m, con subidas a columna y reservas en arquetas.

```latex
\Delta U = \frac{2 \cdot L \cdot I}{\gamma \cdot S} \qquad I = \frac{8\ \text{W}}{24\ \text{V}} = 0{,}33\ \text{A} \quad L = 350\ \text{m} \quad \gamma_{Cu} = 56
```

| Sección (mm²) | ΔU (V) | ΔU (%) | Valoración |
| --- | --- | --- | --- |
| 2,5 | 1,65 | 6,9 | Insuficiente con batería baja |
| 4 | 1,03 | 4,3 | Justa |
| **6** | **0,69** | **2,9** | **Elegida: margen holgado** |

Los módulos LED de 24 V suelen admitir un rango de entrada amplio; verificarlo en la ficha del modelo elegido.

**Canalización**

- 2 tubos TPC Ø90 mm de doble pared, uno de reserva.
- Zanja de 0,40 × 0,60 m en terreno o acera y 0,80 m de profundidad en el cruce de calzada, con hormigón HM-20 y cinta señalizadora.
- Arquetas de 40 × 40 cm con tapa de fundición cada 40 m como máximo, en cambios de dirección y a ambos lados del cruce: unas 11 unidades.
- El trazado cruza un ramal de la intersección con la LP-3; ese tramo va hormigonado.

**Protecciones**

- Protector de sobretensiones tipo 2 para 24 V cc en ambos extremos del cable (armario y caja de la señal). Un cable enterrado de 350 m capta sobretensiones inducidas por rayos.
- Protector de sobretensiones en el lado cc de los módulos FV.
- Fusible de 15 A en bornes de batería y magnetotérmicos cc por circuito.
- Aunque la MBTS no exige tierra de protección, se recomienda poner a tierra las columnas metálicas y los descargadores.

## 8. Accesibilidad y antivandalismo

Todo lo que el público puede tocar es antivandálico (IK10, IP67) y accesible. Lo que no necesita tocar queda fuera de su alcance.

| Elemento | Medida |
| --- | --- |
| Pulsador | Inox Ø30 mm, IK10/IP67, a 0,90–1,20 m de altura, con contraste cromático, pictograma en relieve y Braille |
| Confirmación | Doble: zumbador (personas con discapacidad visual) y piloto ámbar (personas con discapacidad auditiva) |
| Pilotos | LED 22 mm antivandálicos IP67, a 1,40–1,60 m, legibles a pleno sol |
| Placa de instrucciones | Texto breve, pictogramas y Braille: "Pulse para avisar a la próxima guagua" |
| Uso indebido | Las pulsaciones repetidas se ignoran; reset automático a los 90 min; bloqueo de 20 s tras cada reset |
| Armario y batería | En la columna FV con la base a ≈ 1,80 m, cerradura de llave triangular o de seguridad, anclaje interior de la batería |
| Módulos FV | En punta de columna a 4 m, tornillería antirrobo |
| Cableado visto | Empotrado en roza en la fábrica de bloques de la marquesina y por el interior de la columna FV; nada accesible desde el suelo |
| Semáforo | Caja de conexiones con cierre de seguridad y protector de sobretensiones en la base de la columna |

## 9. Mantenimiento y explotación de la prueba piloto

El sistema apenas necesita mantenimiento: limpiar los módulos y revisar el registro del regulador cada trimestre. Durante la prueba piloto se propone un seguimiento de 3 meses para validar el uso real.

| Tarea | Frecuencia | Quién |
| --- | --- | --- |
| Descarga del histórico del regulador por Bluetooth (tensión mínima, días en LVD) | Mensual en la prueba piloto; después trimestral | Mantenedor |
| Limpieza de módulos FV (polvo y calima) | Trimestral, y tras episodios de calima | Mantenedor |
| Prueba funcional con la llave: pulsador, pilotos, zumbador, semáforo y mando | Trimestral | Mantenedor |
| Revisión de protectores de sobretensión, bornes y estanqueidad del armario | Anual | Mantenedor |
| Comprobación de tapas de arquetas y estado del cableado | Anual | Mantenedor |
| Sustitución de la batería LiFePO4 | Previsible a los 10–15 años | Mantenedor |
| Alta y baja de mandos en el receptor | Cuando se requiera | Operador de guaguas |

**Indicadores de la prueba piloto:** avisos por día, tiempo medio entre aviso y reset, número de resets automáticos (avisos no atendidos) y días con la batería por debajo del 30 %. El autómata puede contar los avisos y los resets; si se quiere un registro remoto, se puede añadir un módulo de comunicación móvil.

## 10. Lista de materiales

| Ud. | Elemento | Especificación |
| --- | --- | --- |
| 2 | Módulo FV | 200 Wp monocristalino, 2 en serie (Vmp ≈ 40 V) |
| 1 | Soporte FV | En punta de columna FV, 50° al sur, tornillería antirrobo |
| 1 | Columna FV | Galvanizada 4 m con cimentación HM-20 0,80×0,80×1,00 m; soporta módulos y armario (base a ≈ 1,80 m). Pulsador y pilotos fijados a la marquesina de fábrica de bloques con anclaje químico, cableado empotrado en roza |
| 1 | Armario | Poliéster IP66 ≈ 600 × 500 × 250 mm en la columna FV, cerradura, ventilación y techo parasol; aloja batería, regulador, autómata y protecciones |
| 1 | Regulador MPPT | 100/20, 24 V, salida de carga con LVD y Bluetooth (p. ej. Victron SmartSolar 100/20) |
| 1 | Batería | LiFePO4 25,6 V 100 Ah con BMS |
| 1 | Autómata | Siemens LOGO! 12/24 RCE (salidas a relé) o equivalente |
| 1 | Receptor de radio | 433,92 MHz con código variable (rolling code), 12/24 V, salida a relé, antena exterior |
| 5 | Mandos | 433,92 MHz con código variable, uno por vehículo o conductor |
| 1 | Pulsador | Antivandálico inox Ø30 mm, IP67/IK10, pictograma en relieve y Braille |
| 2 | Pilotos | LED 22 mm 24 V cc antivandálicos IP67, verde y ámbar |
| 1 | Zumbador | 24 V cc, confirmación acústica |
| 1 | Llave de mantenimiento | Interruptor de llave: reset y prueba |
| 1 | Placa de instrucciones | En la parada, con texto en Braille |
| 1 | Semáforo | Semáforo de 2 focos LED Ø200 mm 24 V cc (ámbar y verde), pictograma de bus, viseras, ≈ 8 W por foco |
| 1 | Placa complementaria | "PARADA SOLICITADA", retrorreflectante |
| 1 | Columna semáforo | Galvanizada ≈ 3 m con cimentación y caja de conexiones |
| 3 | Protectores de sobretensión | 2 de tipo 2 a 24 V cc (armario y señal) y 1 en el lado FV |
| 1 | Protecciones cc | Fusible de batería 15 A y magnetotérmicos cc por circuito |
| 350 m | Cable | RV-K 0,6/1 kV 4×6 mm² |
| 15 m | Cable de control | RV-K 0,6/1 kV 7×1,5 mm² armario–marquesina (pulsador, pilotos, zumbador), en tubo Ø63 de 10 m |
| 2 × 320 m | Tubo | TPC Ø90 mm doble pared |
| ≈ 11 | Arquetas | 40 × 40 cm con tapa de fundición |

## 11. Presupuesto estimativo

El presupuesto base de licitación estimado es de **29.254,19 € (IGIC incluido)**. Sirve de estimación para la petición de ofertas. El detalle por partidas, con mediciones y precios unitarios, se recoge en el Anexo I.

| Cap. | Descripción | Importe (€) | % |
| --- | --- | --- | --- |
| 1 | Obra civil y reposición de pavimentos | 13.089,00 | 57,0 |
| 2 | Generación FV y acumulación (incl. columna de 4 m) | 2.853,60 | 12,4 |
| 3 | Control y elementos de la parada | 1.835,00 | 8,0 |
| 4 | Semáforo en carretera | 1.560,00 | 6,8 |
| 5 | Cableado y puesta a tierra | 3.437,50 | 15,0 |
| 6 | Seguridad y salud | 200,00 | 0,9 |
|  | **Presupuesto de ejecución material (PEM)** | **22.975,10** | 100 |
|  | Gastos generales 13 % | 2.986,76 |  |
|  | Beneficio industrial 6 % | 1.378,51 |  |
|  | **Presupuesto base sin IGIC** | **27.340,37** |  |
|  | IGIC 7 % | 1.913,83 |  |
|  | **Presupuesto base de licitación** | **29.254,19** |  |

## 12. Cronograma

La instalación se ejecuta en 2 semanas (10 días hábiles) desde el inicio de obra. Tras la puesta en servicio comienza la prueba piloto.

&#91;embedded content: Cronograma de ejecución por días hábiles\]

El plazo cuenta desde que se dispone de la autorización de obras en la LP-3 y de los materiales en obra, en especial el semáforo. Las cimentaciones se ejecutan en la primera semana para que el hormigón haya fraguado antes del montaje de las columnas. El cruce de calzada se programa en un solo día, en horario de poco tráfico.

## 13. Planos y esquemas

Los planos, en formato A3, se recogen en el Anexo II.

| Nº | Plano | Escala | Contenido |
| --- | --- | --- | --- |
| P-01 | Situación y emplazamiento | Aprox. 1:1.000 | Ortofoto IDECanarias con trazado de la zanja, cruce de calzada, 11 arquetas, marquesina, columna FV y semáforo, coordenadas UTM |
| P-02 | Esquema unifilar de corriente continua | S/E | Generador FV, MPPT, batería, protecciones, circuitos C1–C3, líneas 4×6 y 7×1,5 mm², descargadores |
| P-03 | Esquema de control | S/E | Conexionado del LOGO! (I1–I3, Q1–Q4), diagrama de funciones, tabla de estados |
| P-04 | Detalles de obra civil | Indicada | Zanja en terreno, cruce de calzada, arqueta 40×40 y cimentaciones de las columnas FV y del semáforo |
| P-05 | Alzados | 1:30 | Marquesina con panel de usuario, columna FV de 4 m con armario y columna del semáforo |
