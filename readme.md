# API Indentifacação do BI e NIF

## EndPoints

### **Root**

- default (Read the first observation on top of this doc)

| Method | Endpoint |
| :---: | :---: |
| `GET` | `https://ka6xhw.deta.dev/` |

`Response`

```json
{
    "Validate BI": "https://ka6xhw.deta.dev/bi/{bi}",
    "Validate NIF": "https://ka6xhw.deta.dev/nif/{nif}",
    "Details about maintainer": "https://ka6xhw.deta.dev/about/" 
    }
```

### **About**

| Method | Endpoint |
| :---: | :---: |
| `GET` | `https://ka6xhw.deta.dev/about/` |

`Response`

```json
{
Name: "Paulo Lopes Estevão",
Developer: "Back-End Developer",
Repository: "https://github.com/Paulo-Lopes-Estevao/Api_Identity",
Midia Social: {
    Github: "https://github.com/Paulo-Lopes-Estevao",
    Facebook: "https://facebook.com/paulodoposter.poster.1",
    Linkedin: "https://www.linkedin.com/in/ paulo-lopes-estev%C3%A3o-7a70881b4/",
    Telegram: "https://t.me/Paulo_LopesEstevao"
}
}
```

### **BI**

| Method | Endpoint |
| :---: | :---: |
| `GET` | `https://ka6xhw.deta.dev/bi/{bi}` |

`On Success`

```json
{
    "ID_NUMBER": "",
    "FIRST_NAME": "",
    "LAST_NAME": "",
    "GENDER_NAME": "",
    "BIRTH_DATE": "",
    "FATHER_FIRST_NAME": "",
    "FATHER_LAST_NAME": "",
    "MOTHER_FIRST_NAME": "",
    "MOTHER_LAST_NAME": "",
    "MARITAL_STATUS_NAME": "",
    "BIRTH_PROVINCE_NAME": "",
    "BIRTH_MUNICIPALITY_NAME": "",
    "ISSUE_DATE": "",
    "EXPIRY_DATE": "",
    "ISSUE_PLACE": "",
    "RESIDENCE_COUNTRY_NAME": "",
    "RESIDENCE_PROVINCE_NAME": "",
    "RESIDENCE_MUNICIPALITY_NAME": "",
    "RESIDENCE_COMMUNE_NAME": "",
    "RESIDENCE_NEIGHBOR": "",
    "RESIDENCE_ADDRESS": "",
}
```

`On Error`

```json
{
    False
}
```

### **NIF**

| Method | Endpoint |
| :---: | :---: |
| `GET` | `https://ka6xhw.deta.dev/nif/{nif}` |

`On Success`

```json
{
    True
}
```

`On Error`

```json
{
    False
}
```

## **DOCS Swagger UI**

- <https://ka6xhw.deta.dev/docs>
- <https://ka6xhw.deta.dev/redoc>
