import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetchAndFilterPosts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        filteredByTitle = [
            post for post in posts if len(post['title'].split()) <= 6
        ]

        filteredByBody = [
            post for post in filteredByTitle if len(post['body'].split('\n')) <= 3
        ]

        print("\n GET Result:")
        for post in filteredByBody:
            print(f"id: {post['id ']}, Title: {post['title']}, Body: {post['body'][:50]}...")
        return filteredByBody
    else:
        print("Get request  failed: ", response.status_code)


def createNewPost():
    
    newPost = {
        "title": " new post ",
        "body": "The body of the new post",
        "userID": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=newPost)
    if response.status_code == 201:
        print("\nPOST Result:", response.json())
        return response.json()
    else:
        print("Post request failed:", response.status_code)


def updateExistingPost(postId):
    
    updatedPost = {
        "id": postId,
        "title": "An updated title",
        "body": "Updated body ",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{postId}", json=updatedPost)
    if response.status_code == 200:
        print("\nPUT Result:", response.json())
        return response.json()
    else:
        print("PUT request failed:", response.status_code)


def deleteExistingPost(postId):
    response = requests.delete(f"{BASE_URL}/posts/{postId}")
    if response.status_code == 200:
        print(f"\nDELETE Result, Post with ID {postId} deleted.")
    else:
        print("DELETE request failed:", response.status_code)


if __name__ == "__main__":
    print("Performing GET Request...")
    filteredPosts = fetchAndFilterPosts()

    print("\nPerforming POST Request...")
    createdPost = createNewPost()

    if createdPost:
        print("\nPerforming PUT Request...")
        updateExistingPost(createdPost['id'])

        print("\nPerforming DELETE Request...")
        deleteExistingPost(createdPost['id'])
