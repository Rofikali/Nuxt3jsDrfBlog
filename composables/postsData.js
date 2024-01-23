import { ref } from 'vue'
// import axios from 'axios';

export default function useShowPosts(url = 'http://127.0.0.1:8000/posts', id = null) {
    // const posts_url = 'http://127.0.0.1:8000/'
    const { pending, data: posts, error } = useLazyFetch(url);

    const getPosts = async () => {

        try {
            console.log('posts is her', posts);
            posts
        } catch (error) {
            console.log('error is her', error);
            error
        }
    }

    return {
        // all about posts 
        posts,
        pending,
        error,
        getPosts,
    }
}