import { ref } from 'vue'
import axios from 'axios';


export default function useShowPosts() {
    const url = 'http://127.0.0.1:8000/'
    // const slug = ref([])
    const allposts = ref([])
    const error = ref(null)


    const getPosts = async () => {
        // slug = ref([])
        allposts.value = []
        // error.value = []

        try {
            const res = await axios(url)
            console.log('response is her', res.data);
            allposts.value = res.data
        } catch (err) {
            console.log('error block is here.');
        }

    }

    return {
        allposts,
        getPosts,
    }
}