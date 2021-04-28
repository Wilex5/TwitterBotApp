import tweepy as tw

consumer_key= input("Api Key : ")
consumer_secret= input("Api Secret Key : ")
access_token= input("Access Token : ")
access_token_secret= input("Access Secret Token : ")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



def reponse(nombre_de_reponses, response, search_words, langue):
    i = 0

    tweets = tw.Cursor(api.search, q=search_words, lang=langue).items(nombre_de_reponses)
    for tweet in tweets:
        i += 1
        texte = tweet.text
        tweetid = tweet.id
        api.update_status(response, in_reply_to_status_id = tweetid, auto_populate_reply_metadata=True)
        print(" ")
        print("--------------------")
        print(" ")
        print("Tweet n°", i)
        print(" ")
        print(texte)
    print(" ")
    print(" --------------- ")
    print(" finish ! ")



def finish(nombre_de_reponses, fin, response, langue):
    i = 0
    a = 0

    tweets = tw.Cursor(api.search, q=fin, lang=langue).items(200)
    for tweet in tweets:
        a += 1
        texte = tweet.text
        taille = len(fin)
        taille = taille * -1
        taille -= 2
        last = texte[taille::]
        if fin in last:
            i += 1
            if i != nombre_de_reponses:
                print(" ")
                print("--------------------")
                print(" ")
                print("Tweet n°", a)
                print(" ")
                tweetid = tweet.id
                api.update_status(response, in_reply_to_status_id = tweetid, auto_populate_reply_metadata=True)
                print(tweet.text)
            else:
                print(" ")
                print("---------------------------")
                print(" ")
                print(" finish ! ")
                break




choice = input("(finish / reply) #> ")

if choice == "finish":
    nombre_de_reponses = int(input("Number of reply : "))
    fin = input("The end of the Tweet : ")
    response = input("Your Tweet Reply : ")
    langue = input("The language of the research (fr / en / ...) : ")
    finish(nombre_de_reponses, fin, response, langue)

elif choice == "reply":
    nombre_de_reponses = int(input("Number of reply : "))
    search_words = input("Research : ")
    response = input("Your Tweet Reply : ")
    langue = input("The language of the research (fr / en / ...) : ")
    reponse(nombre_de_reponses, response, search_words, langue)