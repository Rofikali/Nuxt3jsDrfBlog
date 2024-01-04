import { ref } from 'vue'
// import axios from 'axios';

export default function useShowPosts() {
    const posts_url = 'http://127.0.0.1:8000/'
    const { pending, data: posts, error } = useLazyFetch(posts_url);

    // const posts = ref();
    // const pending = ref();
    // const error = ref();
    // const url = ref('');


    const getPosts = async () => {

        try {
            // const res = await axios(url)
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