YouTube Clone Proyektimizni boshlab oldik!

Configuratsiya to'g'irlash

Modellar Yozish 

Api chiqarish barcha Modellarga 

Proyektni yakunlash!

Applar = {
    common
    user
    youtube
}

Modellar

App Common

BaseModel = {
    is_active
    created_at
    updated_at
}

Category = {
    name
}

Country = {
    name
}

Tag = {
    name
}

Channel = {
    author
    name
    channel_link
    description
    image
}

Subscription = {
    user
    channel
}

PlayList = {
    user
    name
}

App User

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
App YouTube

Content = {
    name
    author
    content_link
    slug
    description
    image
    video
    tags
    category
    channel
    language
    country
    like_count
    dislike_count
    play_list
    forward_count
    published_at
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
    to_user
    from_user
}

SavedForLater = {
    user
    content
}
