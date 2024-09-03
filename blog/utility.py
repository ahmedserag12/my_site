from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "ahmed.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Technology in Everyday Life: Technology has become an integral part of our daily routines.
            From smartphones that connect us with the world in an instant to smart home devices that automate household
            chores,
            technology continues to reshape our lifestyles. While it brings convenience and efficiency,
            it also presents challenges such as data privacy and the need for digital literacy.
            Striking a balance between embracing technological advancements and
            maintaining personal security is crucial in today's digital age.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "ahmed2.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - "
                   "that's what happened to me yesterday...",
        "content": """
            The Importance of Reading: Reading opens up a world of imagination, knowledge, and empathy.
            Whether it's a gripping novel, an insightful non-fiction book, or a thought-provoking article,
            reading helps us to understand different perspectives and cultures. It sharpens our minds,
            enriches our vocabulary, and stimulates our creativity. In a fast-paced world dominated by visual media,
            taking the time to read allows us to slow down and immerse ourselves in a world of ideas and stories.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "ahmed3.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
            The Power of Nature: Nature has a profound impact on our well-being. A walk through a forest, listening to
            the rustling leaves and birdsong, can be incredibly rejuvenating. The fresh air, natural light, and serene
            landscapes offer a perfect escape from the hustle and bustle of city life. Studies have shown that spending
            time in nature reduces stress, improves mood, and enhances overall health. It's a reminder of the importance
            of preserving our natural environments for future generations.
        """
    },
    {
        "slug": "into-traveling",
        "image": "baki.png",
        "author": "Ahmed",
        "date": date(2024, 8, 5),
        "title": "Travel At Its Best",
        "excerpt": "Travel is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
            Travel and Exploration: Exploring new places
            can be one of life's most exhilarating experiences.
            From the bustling streets of a foreign city to the
            serene landscapes of remote mountains, every destination
            has its unique charm. Traveling not only broadens one's horizons but also fosters a deeper appreciation for
            diverse cultures and ways of life. Whether it's tasting local cuisines or engaging
            with residents, every journey offers countless
            opportunities to create unforgettable memories.
    """
    }
]


def get_date(post):
    return post['date']
