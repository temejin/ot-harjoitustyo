```mermaid
sequenceDiagram
	participant main
	participant H as HKLLaitehallinto
	participant R as Rautatietori
	participant 6 as ratikka6
	participant 244 as bussi244
	participant L as Lippuluukku
	participant K as Kallen_kortti
	main ->> H: HKLLaitehallinto()
	H -->> main: 	
	main ->>R: Lataajalaite()
	R -->> main: rautatietori
	main ->> 6: Lukijalaite()
	6 -->> main: bussi6	
	main ->> 244: Lukijalaite()
	244 -->> main: bussi244
	main ->>+ H: lisaa_lataaja(rautatietori)
	H -->>- main: 	
	main ->>+ H: lisaa_lukija(ratikka6)
	H -->>- main: 	
	main ->>+ H: lisaa_lukija(bussi244)
	H -->>- main: 	
	main ->> L: Kioski()
	L -->> main: 	
	main ->>+ L: osta_matkakortti("Kalle")
	L ->> K: Matkakortti("Kalle")
	K -->> L: kallen_kortti
	L -->>- main: kallen_kortti
	main ->>+ R: lataa_arvoa(kallen_kortti, 3)
	R ->>+ K: kasvata_arvoa(3)
	K -->>- R: 	
	R -->>- main: 	
	main -->>+ 6: osta_lippu(kallen_kortti, 0)
	6 ->>+ K: vahenna_arvoa()
	K -->>-6: 	
	6 -->>- main: True
	main ->>+ 244: osta_lippu(kallen_kortti, 2)
	244 -->>- main: False
```
