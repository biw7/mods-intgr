def titulo(url):
    urls = url[8:]
    sep = urls.split('/')
    titulo = sep[1]
    return titulo[:12]