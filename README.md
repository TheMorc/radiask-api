***Tento repozitár nemá nijak poškodzovať spoločnosť Apptives a Radia.sk a ani ich oficiálnu aplikáciu z ktorej bolo spracované toto API.***

**Použitie API z tohoto dokumentu nemusí byť povolené spoločnosťami pre neoficiálne aplikácie!**

# Radia.sk API
Dosť jednoduché API použité v iOS a Android aplikáciách Radia.sk

* Pôvodne na využitie v rôznych neoficiálnych aplikáciach pre SailfishOS a iné rôzne platformy na ktoré neexistuje žiadna oficiálna aplikácia.
* Z natúry API nedúfam že sa len tak pokazí *(čož dúfajme že sa ani nikdy nestane)*

Funkčné príklady využitia tohto API:
* **[Pythonový bastl v tomto repozitári](https://github.com/TheMorc/radiask-api/blob/main/radiask.py)**

## Prispievanie do repozitára
Keď vám nejaká podstatná vec chýba, chcete niečo doplniť tak kľudne do toho, potom môžete poslať pull request s novými informáciami.
Každá doplnená vec sa ráta.

## Autor
V prípade záujmu môžete poslať otázku/dopyt/čokoľvek do Issues sekcie tu v tomto repozitári.

**Richard Gráčik - Morc** ([@TheMorc](https://github.com/TheMorc))

## Popis API *(možno moc nečítateľný)*
* xml formát, jednoduchý http request, netreba žiadne authy a záležitosti naokolo
 
### výpis všetkých staníc
`http://api.radia.sk/app/init/ios/3.0.0/?lid=FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF`
* response má výpis staníc, aktuálne hranú pesničku ak vôbec nejaká hrá, stream adresy, ikony a album arty
```xml
<?xml version="1.0" encoding="utf-8"?>
<radia>
	<radio>
		<id>
			<![CDATA[45]]>
		</id>
		<orderString>
			<![CDATA[7]]>
		</orderString>
		<name>
			<![CDATA[Rádio 7]]>
		</name>
		<logo>
			<![CDATA[http://www.radia.sk/_radia/loga/app/7.png?1637011082]]>
		</logo>
		<onairSongAvailable>
			<![CDATA[true]]>
		</onairSongAvailable>
		<onairSong>
			<displayInfo>
				<![CDATA[1]]>
			</displayInfo>
			<artist>
				<![CDATA[Lincoln Brewster]]>
			</artist>
			<title>
				<![CDATA[Made New]]>
			</title>
			<albumImage>
				<![CDATA[https://i.scdn.co/image/ab67616d00001e02be3c0c3c0928e99684d93ea7]]>
			</albumImage>
			<timestamp>
				<![CDATA[1643592303]]>
			</timestamp>
		</onairSong>
		<streams>
			<stream>
				<idFormat>
					<![CDATA[1]]>
				</idFormat>
				<format>
					<![CDATA[MP3]]>
				</format>
				<bitrate>
					<![CDATA[128]]>
				</bitrate>
				<url>
					<![CDATA[https://play.radio7.sk/128]]>
				</url>
			</stream>
		</streams>
	</radio>
</radia>
```
