# Informe de idoneidad – Marquesina Sunfer PR2 en el Roque de los Muchachos

Oct 14, 2026 · @Alberto de Paz Bethencourt

## Objeto y conclusión

La marquesina Sunfer PR2 con chapa, en su configuración de cálculo de **150 km/h de viento y 65 kg/m² de nieve**, cumple frente al viento en el Roque de los Muchachos (La Palma, unos 2.400 m). Frente a la nieve también cumple para los espesores habituales registrados (20-30 cm de nieve reciente, unos 20-45 kg/m²); las acumulaciones locales de hasta 70 cm de diciembre de 2024 se consideran excepcionales. Además deben cerrarse los puntos pendientes de este informe.

La combinación de 130 km/h y 70 kg/m² está en la misma situación, con menos margen frente al viento.

Este informe es una comprobación previa con datos publicados y la documentación del fabricante. No sustituye al cálculo estructural firmado por un técnico competente.

## Datos del producto

Según el manual de montaje del PR2 con chapa (rev. R2-01/25), se analizan dos combinaciones de cálculo de viento y nieve de Sunfer. La sobrecarga de uso de 40 kg/m² es no concomitante y no es carga de nieve.

| Combinación | Viento (km/h) | Nieve (kg/m²) | Resultado en el Roque |
| --- | --- | --- | --- |
| A | 150 | 65 | Viento: cumple. Nieve: cumple |
| B | 130 | 70 | Viento: cumple. Nieve: cumple |

Características principales:

- Inclinación 5°, altura libre 2,265 m, 5 m entre pórticos.
- Pilares, vigas y correas de acero S275 galvanizado en caliente (UNE-EN ISO 1461).
- Cubierta de chapa prelacada de 0,5 mm; perfilería de aluminio EN AW 6005A T6; tornillería inoxidable A2-70.
- Cálculo realizado con Cype 3D. La certificación expresa del documento se refiere a la cimentación.
- Pendiente máxima del terreno: 2 % continuo entre pórticos extremos.

## Condiciones del emplazamiento

El dato oficial de viento más alto en el Roque es una racha de 128 km/h (febrero de 2020), registrada por la estación AEMET C101A a 2.223 m, con datos desde noviembre de 2019.

**Viento**

- CTE DB SE-AE: Canarias en zona eólica C, velocidad básica 29 m/s (unos 104 km/h, media de 10 minutos).
- AEMET C101A: racha máxima de 128 km/h en unos 6,5 años de registro; el resto de meses, entre 66 y 106 km/h.
- La web del telescopio MAGIC cita temporales de hasta 55 m/s (unos 200 km/h). No es un registro oficial y no se usa en la comprobación.
- Emplazamiento en cresta: el efecto topográfico puede aumentar el viento respecto al de la estación.

**Nieve**

- El valor municipal de Garafía (0,2 kN/m²) corresponde a la altitud del casco (387 m) y no representa la cumbre.
- Nieva casi todos los inviernos. En diciembre de 2024 la primera mañana dejó 5-8 cm, pero la nieve llegó a 70 cm en algunos puntos y la LP-4 estuvo cerrada del 23 al 27 de diciembre. En diciembre de 2022 se acumularon unos 30 cm.
- La acumulación por viento (ventisqueros) y la lluvia sobre nieve pueden elevar la carga real sobre una cubierta de 5°.

**Otros factores**

- Ciclos frecuentes de hielo y deshielo (mínimas de hasta unos -8 °C).
- Densidad del aire a 2.400 m de unos 0,96 kg/m³, frente a 1,25 kg/m³ a nivel del mar: reduce la presión del viento en torno a un 23 %.

## Comprobación de cargas

La combinación de 150 km/h equivale a unos 171 km/h en la cumbre, un 34 % por encima de la racha máxima oficial de 128 km/h.

La velocidad equivalente en el sitio corrige la menor densidad del aire: v sitio = v cálculo × √(1,25 / 0,96) ≈ v cálculo × 1,14. Se supone que la velocidad de cálculo de Sunfer está referida a nivel del mar y es comparable con una racha; está pendiente de confirmar.

| Combinación | Viento de cálculo (km/h) | Equivalente en el Roque (km/h) | Margen frente a 128 km/h | Nieve de cálculo (kg/m²) |
| --- | --- | --- | --- | --- |
| A | 150 | 171 | +34 % | 65 |
| B | 130 | 148 | +16 % | 70 |

**Viento.** La combinación A deja margen frente a lo medido. Aun así, la serie oficial es corta y el valor de proyecto debe ser el extremo a 50 años en la ubicación exacta, previsiblemente superior a 128 km/h.

**Nieve.** No existen mediciones de carga de nieve (kg/m²) en el Roque; lo publicado son espesores: unos 30 cm en diciembre de 2022 y hasta 70 cm en puntos concretos en diciembre de 2024. Convertidos con densidades típicas de 100 a 350 kg/m³, darían entre unos 30 y 245 kg/m², un rango que incluye los 65-70 kg/m² de cálculo pero que es una estimación, no un registro. Con 5° de inclinación la nieve no resbala de la cubierta. Nieve: cumple para los espesores habituales registrados (20-30 cm de nieve reciente, unos 20-45 kg/m²), por debajo de los 65-70 kg/m² de cálculo. Las acumulaciones locales de hasta 70 cm de diciembre de 2024 se consideran excepcionales.

**Cargas totales (combinación A).** La carga vertical total sin mayorar es del orden de 90 kg/m²: peso propio más nieve. La sobrecarga de uso no se suma porque es no concomitante.

| Carga | Valor aprox. (kg/m²) | Tipo |
| --- | --- | --- |
| Peso propio (acero, chapa y paneles) | \~25 | Permanente |
| Nieve | 65 | Variable (determinante) |
| Uso (mantenimiento) | 40 | Variable, no concomitante: no se suma |
| Total vertical sin mayorar | \~90 |  |
| Total vertical mayorado (1,35·PP + 1,5·N) | \~130 | Valor de dimensionado (ELU) |

El peso propio se estima a partir de las reacciones del manual (0,648 t en la zapata central, con unos 5 m entre pórticos y 5-5,6 m de cubierta); el valor exacto debe facilitarlo Sunfer. El viento se combina con la nieve mediante los coeficientes de combinación del CTE; el caso más desfavorable para anclajes es la succión (0,9·PP − 1,5·V).

**Aclaración: capacidad máxima en un momento crítico.** Los valores garantizados por el fabricante son 65 kg/m² de nieve sobre el peso propio (unos 90 kg/m² en total; unos 45-65 cm de nieve reciente o 25 cm de nieve asentada) y 150 km/h de viento (unos 170 km/h equivalentes en la cumbre).

Por los coeficientes de seguridad del cálculo (1,5 sobre nieve y viento), el colapso teórico se situaría por encima de unos 100 kg/m² de nieve y de unos 185 km/h de viento a nivel del mar (unos 210 km/h en la cumbre). Este margen cubre incertidumbres de material, ejecución y estimación de cargas, y no constituye capacidad de reserva utilizable como valor de diseño.

En una situación extrema de viento, el elemento previsiblemente más solicitado es la unión pilar-zapata (pernos M16 a tracción). La cifra exacta de rotura requiere los índices de aprovechamiento del cálculo de Sunfer en Cype 3D.

## Cimentación y anclajes

Con la combinación A, el viento más desfavorable (hipótesis V6) levanta los pilares: la succión supera al peso propio de la estructura, y los pernos trabajan a tracción.

| Zapata | Peso propio Rz (t) | Viento V6 Rz (t) | Neto sin mayorar (t) | Neto mayorado 0,9·PP + 1,5·V (t) | Peso de la zapata (t) |
| --- | --- | --- | --- | --- | --- |
| Extremos | 0,530 | -0,564 | -0,034 | -0,369 | 2,6-3,1 |
| Central | 0,648 | -0,741 | -0,093 | -0,529 | 2,9-3,6 |

El peso de la zapata se estima con hormigón de 2,5 t/m³ y las dimensiones del manual (1,60-1,90 m de lado, 0,40 m de canto, según la tensión del terreno). Las zapatas tienen margen frente al levantamiento; el punto crítico es la unión pilar-zapata.

- Pernos de gancho M16, 300 mm embebidos más 100 mm vistos, calidad 8.8 si son cincados o A2-70 si son inoxidables. No los suministra Sunfer.
- Placa base de 400 × 300 × 12 mm, con mortero de nivelación sin retracción de 10 a 40 mm y apriete a 140 Nm.
- El manual especifica hormigón C25/30 en ambiente XC2, que no contempla ciclos de hielo y deshielo.
- Las zapatas están dimensionadas para terrenos de 0,5 a 2 kg/cm²; la tensión admisible real debe salir de un estudio geotécnico.

## Puntos pendientes y recomendaciones

Hay que pedir a Sunfer expresamente la combinación de 150 km/h y 65 kg/m² y cerrar estos seis puntos antes de ejecutar.

- [ ] **Alcance del certificado.** Confirmar por escrito que pilares, vigas, correas y chapa, no solo la cimentación, están calculados para 150 km/h y 65 kg/m², y si los 150 km/h son racha o velocidad básica del CTE.
- [ ] **Viento y nieve a 50 años.** Que el técnico firmante estime ambos valores en la ubicación exacta, incluido el efecto topográfico de cresta.
- [ ] **Hormigón resistente a heladas.** Sustituir el ambiente XC2 por una clase XF, con aireante y baja relación agua/cemento.
- [ ] **Estudio geotécnico.** Verificar la tensión admisible del terreno y ajustar las zapatas si queda fuera de 0,5-2 kg/cm².
- [ ] **Pendiente del terreno.** Garantizar como máximo un 2 % continuo entre pórticos extremos, con explanación si hace falta.
- [ ] **Paneles.** Comprobar en la ficha del módulo la succión admisible con la fijación usada (61H, 05V, 05.1V o 62V) frente a la succión de cálculo.

En ejecución, cuidar especialmente los pernos de anclaje: posición con plantilla, calidad especificada, mortero bajo placa sin huecos y par de apriete.

## Limitaciones y fuentes

La comprobación se basa en datos publicados y en el manual del fabricante; no incluye cálculo estructural propio ni visita al emplazamiento.

- Manual de montaje Sunfer PR2 con chapa, rev. R2-01/25 (aportado por el cliente).
- [Catálogo Sunfer 2026](https://www.vicoexport.com/wp-content/uploads/2026/07/catalogo-sunfer-es-Q3-vico-export-solar-energy.pdf)
- [Clima en Roque de los Muchachos, estación AEMET C101A (x-y.es)](https://x-y.es/clima/santa-cruz-de-tenerife/C101A-roque-de-los-muchachos)
- [Garafía: datos CTE (Normatia)](https://normatia.com/es/municipios/canarias/santa-cruz-de-tenerife/garafia/)
- [Primera nevada del invierno en La Palma, diciembre de 2024 (elDiario.es)](https://www.eldiario.es/canariasahora/lapalmaahora/sociedad/llega-palma-primera-nevada-invierno_1_11922631.html)
- [MAGIC: el emplazamiento del Roque de los Muchachos](https://magic.mpp.mpg.de/newcomers/magic-site/)
