# Amazon product JSON list 

A python script that generates a list of articles based on a keyword, and optionally can download the associated images.

### How to use

Download a list of articles with the keyword 'gloves'
```
python amazon.py -k gloves
```

### Options

* -k keyword
* -o output file
* -d download images (folder name)
* -p num pages to download

### Example 1

**Download** a list of **2 pages of products with the keyword 'ballon' on** a desktop file named **products.json**
```
python amazon.py -k ballon -p 2 -o ~/Desktop/products.json
```

### Example 2

Download a list of products with the keyword **'jersey'** on a desktop file named **products.json** and create a folder named images with the hiRes images of all the variants.
```
python amazon.py -k jersey -p 2 -o ~/Desktop/products.json -d images
```

### Information per product (when available)

* Title 
* Description
* URL
* Price (Currency and Value)
* amazonID
* List Of Image Preview (you can download hiRes with -d option)
* keywords 
* Rating

### Example Result

```
{
    "title": "iPretty Cardigan Jersey de Punto Mujer Estampado Gr\u00eds Talla 36 38 40 42",
    "url": "http://www.amazon.es/iPretty-Cardigan-Jersey-Punto-Estampado/dp/B015STYT2C",
    "price": {
        "currency": "EUR",
        "value": "12,59"
    },
    "amazonID": "B015STYT2C",
    "details": {
        "images": {
            "Multi": [{
                "large": "http://ecx.images-amazon.com/images/I/41amsbKss2L.jpg",
                "hiRes": "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SL1001_.jpg",
                "main": {
                    "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SX425_.jpg": ["425", "425"],
                    "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SX466_.jpg": ["466", "466"],
                    "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SX522_.jpg": ["522", "522"],
                    "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SY355_.jpg": ["355", "355"],
                    "http://ecx.images-amazon.com/images/I/61BfqrXekNL._SY450_.jpg": ["450", "450"]
                },
                "variant": "MAIN",
                "thumb": "http://ecx.images-amazon.com/images/I/41amsbKss2L._SS40_.jpg"
            }, {
                "large": "http://ecx.images-amazon.com/images/I/41jKqnre-rL.jpg",
                "hiRes": "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SL1001_.jpg",
                "main": {
                    "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SX466_.jpg": ["466", "466"],
                    "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SX425_.jpg": ["425", "425"],
                    "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SY355_.jpg": ["355", "355"],
                    "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SX522_.jpg": ["522", "522"],
                    "http://ecx.images-amazon.com/images/I/51Orm9%2ByUaL._SY450_.jpg": ["450", "450"]
                },
                "variant": "PT01",
                "thumb": "http://ecx.images-amazon.com/images/I/41jKqnre-rL._SS40_.jpg"
            }],
            "Gr\u00eds": [{
                "large": "http://ecx.images-amazon.com/images/I/512NVLi%2BH-L.jpg",
                "hiRes": "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SL1001_.jpg",
                "main": {
                    "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SX522_.jpg": ["522", "522"],
                    "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SX466_.jpg": ["466", "466"],
                    "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SY355_.jpg": ["355", "355"],
                    "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SY450_.jpg": ["450", "450"],
                    "http://ecx.images-amazon.com/images/I/61kLvRG-7NL._SX425_.jpg": ["425", "425"]
                },
                "variant": "MAIN",
                "thumb": "http://ecx.images-amazon.com/images/I/512NVLi%2BH-L._SS40_.jpg"
            }, {
                "large": "http://ecx.images-amazon.com/images/I/41duidIvsgL.jpg",
                "hiRes": "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SL1001_.jpg",
                "main": {
                    "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SX466_.jpg": ["466", "466"],
                    "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SX425_.jpg": ["425", "425"],
                    "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SY450_.jpg": ["450", "450"],
                    "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SY355_.jpg": ["355", "355"],
                    "http://ecx.images-amazon.com/images/I/61tMCtiHm8L._SX522_.jpg": ["522", "522"]
                },
                "variant": "PT01",
                "thumb": "http://ecx.images-amazon.com/images/I/41duidIvsgL._SS40_.jpg"
            }]
        },
        "keywords": ["iPretty Cardigan Jersey de Punto Mujer Estampado Gr\u00eds Talla 36 38 40 42", "iPretty"],
        "description": "<p>Ideales para todas las ocasiones. <br/> Tama\u00f1o: <br/> Tama\u00f1o(cm) Longuitud Hombro Manga Busto Cintura <br/> S/EU36 61 37 60 86 76 <br/> M/EU38 62 38 61 90 80 <br/> L/EU40 64 39 62 94 84 <br/> XL/EU42 65 40 63 98 88 <br/> Nota: <br/> Los colores reales pueden ser distintos a los presentados en la foto.    </p>",
        "rating": "3"
    },
    "thumbnail": "http://ecx.images-amazon.com/images/I/512NVLi%2BH-L._AA160_.jpg"
},
```

### Version
0.1.0


