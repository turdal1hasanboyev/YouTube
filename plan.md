'YouTube' clone proyektimizni boshlab oldik!

Configuratsiya to'g'irlash!

Modellar yozish! 

Api chiqarish barcha modellarga! 

Proyektni yakunlash!

Applar = {
    common
    user
    youtube
}

Modellar!

App common!

BaseModel = {
    is_active
    created_at
    updated_at
}

Category = {
    name
    slug
}

Country = {
    name
    slug
}

Tag = {
    name
    slug
}

Channel = {
    author
    name
    slug
    channel_link
    description
    image
}

Subscription = {
    user
    channel
}

PlayList = {
    name
    slug
}

App user

User = {
    description
    image
    phone_number
    birth_date
    gender
    occupation 
    adress
    followers_count 
    following_count 
    last_active 
    favourite_social_network
}

App youtube

Content = {
    name
    content_link
    slug
    description
    image
    video
    tags
    category
    channel
    content_language
    country
    like_count
    dislike_count
    play_list
    forward_count
    premiere_date
}

Liked = {
    user
    content
    like_or_dislike
}

Comment = {
    user
    content
    comment
}

FriendRequest = {
    from_user
    to_user
}

SavedForLater = {
    user
    content
}

Premiera = {
    premiere_date
    content
}

Proyektni yakunlash Finish Project! commitini qoldirish 

Bugun sana 07.09.2024-yil soat 18:38

Comment - "Default Settings in YouTube Clone Project!"

Asia/Uzbekistan/Tashkent *location

Developer Hasanboyev Turdali (python backend developer)
