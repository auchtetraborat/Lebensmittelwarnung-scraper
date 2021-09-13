## Das Projekt ist mittlerweile in https://github.com/bundesAPI/deutschland integriert. Die Version dort dürfte aktiver weiterentwickelt werden, schaut dort vorbei.
## Das hier ist der Stand zum Zeitpunkt der Integration.

## Scraper für den RSS Feed von https://www.lebensmittelwarnung.de/bvl-lmw-de/

Source: https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/ $type / $region .rss

| $type                     |  Wert                     |
| -------------             | -------------             |
| alle                      | Warnungen aller Typen     |
| lebensmittel              | nur Lebensmittel          |
| kosmetische+mittel        | nur kosmetische Mittel    |
| bedarfsgegenstaende       | nur Bedarfsgegenstände    |
| mittel+zum+taetowieren    | nur Mittel zum Tätowieren |

| $region                     
| -------------             | 
| alle_bundeslaender        |
| baden_wuerttemberg        |
| bayern                    |
| berlin                    |
| brandenburg               |
| bremen                    |
| hamburg                   |
| hessen                    |
| mecklenburg_vorpommern    |
| niedersachsen             |
| nordrhein_westfalen       |
| rheinland_pfalz           |
| saarland                  |
| sachsen                   |
| sachsen_anhalt            |
| schleswig_holstein        |
| thueringen                |


Jede Produktwarnung ist zudem über eine Integer-ID identifiziert. Diese findet ihr im Feld **link** oder **guid** jedes **item**s als letzten Parameter der URL.
```html
<link>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/69535</link>
oder
<guid>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/69535</guid>
```

Anmerkungen:
```html
<link> == <guid>
<description> == <content:encoded>
```

Ergebnis ist ein JSON der Form
```json
{
    "id": number, 
    "guid": string,
    "pubDate": string,
    "imgSrc": string,
    "title": string,
    "manufacturer": string,
    "type": string, 
    "warning": string,
    "affectedStates": [string]
}
```

TODO:
* ~~Scraping nicht nur mit $type = alle && $region = alle_bundeslaender~~ 
* ~~Integration in deutschland?~~ 
* OpenAPI-Spec -> API-Client?