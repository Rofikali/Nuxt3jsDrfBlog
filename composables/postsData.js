import { ref } from 'vue'
import axios from 'axios';


export default function useShowPosts() {
    const url = 'http://127.0.0.1:8000/'
    // const slug = ref([])
    const posts = ref([])
    const error = ref('this is error')


    const getPosts = async () => {

        posts.value = []
        // error.value = []

        try {
            const res = await axios(url)
            console.log('response is her', res.data);
            posts.value = res.data
        } catch (err) {
            console.log('error block is here.', err.value);
        }

    }

    return {
        posts,
        getPosts,
    }
}