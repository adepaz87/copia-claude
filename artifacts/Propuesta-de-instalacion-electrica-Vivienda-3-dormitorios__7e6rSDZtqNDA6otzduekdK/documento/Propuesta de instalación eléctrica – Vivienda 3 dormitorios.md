# Propuesta de instalación eléctrica – Vivienda 3 dormitorios

Oct 26, 2026 · @Alberto de Paz Bethencourt

Se propone una instalación interior de vivienda con **electrificación elevada (9.200 W a 230 V, IGA 40 A)**, 10 circuitos y 3 diferenciales, conforme al REBT (ITC-BT-10, 15, 17, 19, 25, 26 y 27).

## Datos de partida

Vivienda en planta baja con fachada a calle y a propiedad, de unos 70 m² útiles. Superficies estimadas a partir de las cotas del plano (estancias irregulares aproximadas):

| Estancia | Cotas (m) | Superficie aprox. (m²) |
| --- | --- | --- |
| Salón - cocina (incl. zona de entrada) | 7,85 × 1,20 + 6,35 × 3,4 med. | 31,0 |
| Habitación 1 | 3,30 × 2,90 | 9,6 |
| Habitación 2 | 3,20 × 2,90 | 9,3 |
| Habitación 3 | 2,58 med. × 3,60 | 9,3 |
| Baño completo | 1,60 × 2,90 | 4,6 |
| Aseo | 1,40 × 2,90 | 4,1 |
| Cuarto de limpieza | 2,05 × 1,40 (trapecio) | 2,7 |
| **Total útil** |  | **≈ 70,6** |

Supuestos: cocina eléctrica (vitrocerámica de inducción + horno), termo eléctrico, lavadora y secadora en el cuarto de limpieza, y aire acondicionado por splits. Si alguno no aplica, se revisa el grado de electrificación.

## Grado de electrificación y potencia

La vivienda es **electrificación elevada** porque se prevé aire acondicionado y secadora (ITC-BT-25, apdo. 2.2.2), aunque la superficie (< 160 m²) por sí sola admitiría la básica.

- Potencia prevista (ITC-BT-10): **9.200 W** a 230 V.
- Interruptor general automático: **40 A**, 2P, poder de corte ≥ 4,5 kA.
- Potencia a contratar orientativa: 5,75–6,9 kW según uso real del AA; la instalación queda dimensionada para 9,2 kW sin obra adicional.

Si el cliente renuncia a AA y secadora, puede ejecutarse como básica (5.750 W, IGA 25 A, 5 circuitos), pero no se recomienda: el sobrecoste es pequeño y evita reformas futuras.

## Acometida, derivación individual y cuadro general

**Derivación individual (ITC-BT-15):** 2 × 10 mm² + TT 10 mm² Cu, cable H07Z1-K (AS) 450/750 V bajo tubo de 32 mm, más hilo de mando de 1,5 mm² (rojo). Caída de tensión máxima 1 % (contador individual). La sección de 10 mm² cubre 40 A con margen para longitudes de hasta unos 15–20 m; verificar con la distancia real al contador.

**Ubicación del cuadro (ITC-BT-17):** junto a la puerta de entrada desde la calle, en el paramento interior del salón, a 1,40–2,00 m del suelo. Caja empotrada de 2 filas / 24 módulos (deja reserva ≥ 20 %).

**Composición del cuadro:**

1. Hueco para ICP / ICP-M (si lo exige la distribuidora).
2. IGA 2P 40 A, 6 kA.
3. Protector combinado de sobretensiones transitorias y permanentes 2P (ITC-BT-23).
4. Diferencial ID1 2P 40 A 30 mA tipo A → C1, C2, C7.
5. Diferencial ID2 2P 40 A 30 mA tipo A → C3, C4.1, C4.2, C4.3, C5.
6. Diferencial ID3 2P 40 A 30 mA tipo A → C9, C10.
7. PIAs por circuito según el cuadro siguiente.

Se usan diferenciales tipo A por la inducción, lavadora y equipos inverter, que generan corrientes de fuga con componente continua.

## Cuadro de circuitos interiores

Diez circuitos con cable H07Z1-K (AS) bajo tubo corrugado empotrado; sección de tierra igual a la de fase.

| Circuito | Uso | PIA (A) | Sección (mm²) | Tubo Ø (mm) | Diferencial | Puntos |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | Iluminación | 10 | 1,5 | 16 | ID1 | 14 |
| C2 | Tomas uso general salón-cocina, entrada, limpieza | 16 | 2,5 | 20 | ID1 | 9 |
| C7 | Tomas uso general dormitorios (adicional de C2) | 16 | 2,5 | 20 | ID1 | 9 |
| C3 | Cocina inducción y horno | 25 | 6 | 25 | ID2 | 2 |
| C4.1 | Lavadora | 16 | 2,5 | 20 | ID2 | 1 |
| C4.2 | Lavavajillas | 16 | 2,5 | 20 | ID2 | 1 |
| C4.3 | Termo eléctrico | 16 | 2,5 | 20 | ID2 | 1 |
| C5 | Tomas baño, aseo y encimera de cocina | 16 | 2,5 | 20 | ID2 | 6 |
| C9 | Aire acondicionado | 25 | 6 | 25 | ID3 | 4 |
| C10 | Secadora | 16 | 2,5 | 20 | ID3 | 1 |

C4 se desdobla en tres circuitos de 16 A (opción admitida por la ITC-BT-25) para no compartir protección entre lavadora, lavavajillas y termo. C7 no es obligatorio por número de tomas, pero reparte la carga y evita que un fallo en dormitorios deje sin tomas el salón.

Caídas de tensión máximas: 3 % en circuitos interiores. Con estas secciones y recorridos < 15 m se cumple holgadamente.

## Puntos de utilización por estancia

Dotación igual o superior a los mínimos de la tabla 2 de la ITC-BT-25. Las bases dobles cuentan como un punto.

| Estancia | Luz (C1) | Tomas uso general | Tomas específicas |
| --- | --- | --- | --- |
| Entrada / franja de paso (7,85 m) | 2, conmutados desde puerta y fondo | 1 (C2) | — |
| Salón (≈ 20 m²) | 3 (general, comedor, zona TV) | 5 (C2), 2 dobles junto a TV | 1 AA (C9) |
| Cocina (zona del salón) | 2 (general + bajo muebles altos) | 2 (C2): frigorífico y campana; 4 en encimera (C5) | Inducción y horno (C3); lavavajillas (C4.2) |
| Habitación 1 | 1, de cruce (puerta y ambos lados del cabecero) | 3 (C7): 2 a cabecero, 1 escritorio | 1 AA (C9) |
| Habitación 2 | 1, de cruce (puerta y ambos lados del cabecero) | 3 (C7) | 1 AA (C9) |
| Habitación 3 | 1, de cruce (puerta y ambos lados del cabecero) | 3 (C7) | 1 AA (C9) |
| Baño completo | 2 (techo + aplique espejo) | 1 (C5) junto a lavabo | — |
| Aseo | 1 | 1 (C5) junto a lavabo | — |
| Cuarto de limpieza | 1 | 1 (C2) | Lavadora (C4.1), termo (C4.3), secadora (C10) |

Alturas orientativas: mecanismos a 1,10 m, tomas a 0,30 m, tomas de encimera a 1,10 m y salida de split a 2,20 m. La cocina se sitúa contra la pared de la habitación 3 o la medianera con el cuarto de limpieza; confirmar la distribución del mobiliario antes de replantear.

## Baños, puesta a tierra y condiciones de ejecución

**Baño y aseo (ITC-BT-27):**

- Volúmenes 0 y 1: sin mecanismos ni cajas; solo luminarias MBTS ≤ 12 V o IPX4 si están dentro.
- Volumen 2 (0,60 m alrededor de bañera/plato): luminarias clase II e IPX4; sin tomas.
- Tomas del lavabo fuera de volúmenes 0–2, IP44 recomendado. Interruptores fuera del baño o fuera de volúmenes.
- Conexión equipotencial suplementaria solo si hay tuberías o elementos metálicos accesibles.

**Puesta a tierra (ITC-BT-18 y 26):** conexión al borne de tierra del edificio o, si no existe, electrodo con picas de acero-cobre de 2 m y línea de enlace de 16 mm². Medir la resistencia y comprobar que la tensión de contacto con 30 mA no supera 24 V en locales húmedos.

**Ejecución:**

- Tubo corrugado empotrado (ITC-BT-21); cajas de registro y de mecanismo independientes por circuito o con bornas identificadas.
- Colores: azul neutro, marrón/negro/gris fase, verde-amarillo protección.
- Separación mínima de 5 cm con canalizaciones de agua y telecomunicaciones.
- Al finalizar: medición de aislamiento (≥ 0,5 MΩ a 500 V c.c.), continuidad de tierra, disparo de diferenciales y certificado de instalación (CIE) de instalador habilitado, tramitado ante la Dirección General de Industria del Gobierno de Canarias con Memoria Técnica de Diseño (no requiere proyecto).

## Opcionales y observaciones

**Opcionales a ofertar aparte:**

- Preinstalación de punto de recarga de vehículo eléctrico (ITC-BT-52), si hay plaza asociada.
- Iluminación LED empotrada en salón-cocina con regulación.
- Telecomunicaciones: tomas RJ45 y TV en salón y dormitorios, en canalización independiente.
- Domótica básica (C11) o control de splits por wifi.

**Pendiente de confirmar con el cliente:**

- [ ] Ubicación exacta de la cocina y del mobiliario del salón.
- [ ] Si habrá AA en las tres habitaciones o solo preinstalación.
- [ ] Tipo de calentador de agua (termo eléctrico o aerotermia; esta última requeriría un circuito propio de 25 A).
- [ ] Distancia real del contador al cuadro, para validar la sección de la derivación individual.
- [ ] Potencia a contratar.
