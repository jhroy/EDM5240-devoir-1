for a in range(19999,30151):
    
    mc_url= "https://montrealcampus.ca?p={page_number}" .format(page_number = a)
    
    print(mc_url)

    mc_url.append(a)

    print(len(mc_url))
