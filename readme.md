# API Indentifacação do BI e NIF

## EndPoint : 

### **Default**

- default (Read the first observation on top of this doc)

|Method|Endpoint        |
|------|----------------|
|`GET` |`https://ka6xhw.deta.dev`|

<br>

<table>
<tr>
<th>Response</th>
</tr>
<tr>
<td>

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
</td>
</tr>
</table>

### **BI**

- 

|Method|Endpoint        |
|------|----------------|
|`GET` |`https://ka6xhw.deta.dev/bi/{bi}`|

<br>

<table>
<tr>
<th>On Success</th>
<th>On Error</th>
</tr>
<tr>
<td>

```json
{
    True
}

```
</td>
<td>

```json
{
    False
}

```
</td>
</tr>
</table>


### **NIF**

- 

|Method|Endpoint        |
|------|----------------|
|`GET` |`https://ka6xhw.deta.dev/nif/{nif}`|

<br>

<table>
<tr>
<th>On Success</th>
<th>On Error</th>
</tr>
<tr>
<td>

```json
{
    True
}
```
</td>
<td>

```json
{
    False
}

```
</td>
</tr>
</table>

<br>
<br>

## **DOCS Swagger UI**
> https://ka6xhw.deta.dev/docs