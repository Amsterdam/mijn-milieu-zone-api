def get_all_source():
    return [
        {
            "thema": "Milieuzone",
            "categorie": "F2",
            "prioriteit": 50,
            "datum": "2020-02-06",
            "titel": "milieuzone.f2.aanvragen_en_ontheffingen.titel",
            "omschrijving": "milieuzone.f2.aanvragen_en_ontheffingen.omschrijving",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvragen",
            "urlNaam": "milieuzone.f2.aanvragen_en_ontheffingen.button",
        },
        {
            "thema": "Milieuzone",
            "categorie": "F3",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is afgewezen",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/5A158FD9-B07D-4A4C-B780-8359A9A14906",
            "urlNaam": "Meer informatie",
        },
        {
            "thema": "Milieuzone",
            "categorie": "M1",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw moet uw aanvraag ontheffing voor milieuzone Brom/Snor nog betalen",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/88D12139-6BFF-45BF-9FA5-4BFCC01F284F",
            "urlNaam": "Betaal direct",
        },
        {
            "thema": "Milieuzone",
            "categorie": "M1",
            "prioriteit": 0,
            "datum": "2019-12-11",
            "titel": "milieuzone.m1.overtreding.gebied.niet_bekeken.titel",
            "omschrijving": "milieuzone.m1.overtreding.gebied.niet_bekeken.omschrijving",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/overtreding/46B958B6-9F46-4784-A453-716320950454",
            "urlNaam": "milieuzone.m1.overtreding.gebied.niet_bekeken.button",
        },
        {
            "thema": "Milieuzone",
            "categorie": "F3",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is toegekend",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/3A36D276-244D-4B12-8A43-97573502728E",
            "urlNaam": "Meer informatie",
        },
        {
            "thema": "Milieuzone",
            "categorie": "F3",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is afgewezen",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/2A3B4C05-700C-4C1E-A399-4E171F5B5420",
            "urlNaam": "Meer informatie",
        },
        {
            "thema": "Milieuzone",
            "categorie": "F3",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is toegekend",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/7B46A24E-BC21-44F9-ADB8-B85A75FAFB90",
            "urlNaam": "Meer informatie",
        },
        {
            "thema": "Milieuzone",
            "categorie": "M1",
            "prioriteit": 0,
            "datum": "2019-12-13",
            "titel": "Uw aanvraag ontheffing milieuzone Brom/Snor",
            "omschrijving": "Uw moet uw aanvraag ontheffing voor milieuzone Brom/Snor nog betalen",
            "url": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/56B31535-1404-4AC0-8658-CD77C32C12EE",
            "urlNaam": "Betaal direct",
        },
    ]


def get_all_expected():
    return {
        "content": {
            "isKnown": True,
            "meldingen": [
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is afgewezen",
                    "id": "milieu-F3",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Meer informatie",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/5A158FD9-B07D-4A4C-B780-8359A9A14906",
                    },
                },
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw moet uw aanvraag ontheffing voor milieuzone Brom/Snor nog betalen",
                    "id": "milieu-M1",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Betaal direct",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/88D12139-6BFF-45BF-9FA5-4BFCC01F284F",
                    },
                },
                {
                    "datePublished": "2019-12-11",
                    "description": "milieuzone.m1.overtreding.gebied.niet_bekeken.omschrijving",
                    "id": "milieu-M1",
                    "priority": 0,
                    "title": "milieuzone.m1.overtreding.gebied.niet_bekeken.titel",
                    "link": {
                        "title": "milieuzone.m1.overtreding.gebied.niet_bekeken.button",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/overtreding/46B958B6-9F46-4784-A453-716320950454",
                    },
                },
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw aanvraag voor ontheffing milieuzone "
                    "Brom/Snor is toegekend",
                    "id": "milieu-F3",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Meer informatie",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/3A36D276-244D-4B12-8A43-97573502728E",
                    },
                },
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw aanvraag voor ontheffing milieuzone Brom/Snor is afgewezen",
                    "id": "milieu-F3",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Meer informatie",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/2A3B4C05-700C-4C1E-A399-4E171F5B5420",
                    },
                },
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw aanvraag voor ontheffing milieuzone "
                    "Brom/Snor is toegekend",
                    "id": "milieu-F3",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Meer informatie",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/7B46A24E-BC21-44F9-ADB8-B85A75FAFB90",
                    },
                },
                {
                    "datePublished": "2019-12-13",
                    "description": "Uw moet uw aanvraag ontheffing voor milieuzone Brom/Snor nog betalen",
                    "id": "milieu-M1",
                    "priority": 0,
                    "title": "Uw aanvraag ontheffing milieuzone Brom/Snor",
                    "link": {
                        "title": "Betaal direct",
                        "to": "https://ontheffingen-acc.amsterdam.nl/publiek/aanvraag/56B31535-1404-4AC0-8658-CD77C32C12EE",
                    },
                },
            ],
            "tips": [],
        },
        "status": "OK",
    }
