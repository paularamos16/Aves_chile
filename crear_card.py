def crear_card(datos):
    cards=''
    for dato in datos:
        cards += f'''
        <div class="card" style="width: 18rem;">
            <img src="{dato['images']['thumb']}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title"{dato['name']['spanish']}</h5>
                 <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">nombre en ingles:{dato['name']['english']}dato</li>
            <li class="list-group-item">A second item</li>
            <li class="list-group-item">A third item</li>
        </ul>
</div>
'''
    return cards
