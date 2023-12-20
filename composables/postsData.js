import { ref } from 'vue'
// import axios from 'axios';

const route = useRoute()

export default function useShowPosts() {
    const url = 'http://127.0.0.1:8000/'
    const { pending, data: posts, error } = useLazyFetch(url);

    const posts_data = ref();
    const err = ref();

    const getPosts = async () => {

        try {
            // const res = await axios(url)
            console.log('response is her');
            posts = posts_data.value
        } catch (err) {
            err.value
        }
    }

    return {
        posts,
        getPosts,
    }
}