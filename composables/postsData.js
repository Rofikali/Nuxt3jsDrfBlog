import { ref } from 'vue'
import axios from 'axios';

const route = useRoute()

export default function useShowPosts() {
    const url = 'http://127.0.0.1:8000/'
    const { pending, data: posts, error } = useLazyFetch(url);

    const posts_data = ref();

    const getPosts = async () => {

        if (pending) {
            console.log('pending ... PostsData', pending);
        } else {
            posts = posts_data.value
        }

        // try {
        //     posts = posts
        //     console.log('response is her', posts);
        // } catch (err) {
        //     console.log('error block is here.', err.error);
        // }

    }
    // const getPosts = async () => {

    //     posts.value = []
    //     // error.value = []

    //     try {
    //         const res = await axios(url)
    //         console.log('response is her', res.data);
    //         posts.value = res.data
    //     } catch (err) {
    //         console.log('error block is here.', err.value);
    //     }

    // }

    return {
        posts,
        getPosts,
    }
}