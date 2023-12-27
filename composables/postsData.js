import { ref } from 'vue'
// import axios from 'axios';

const route = useRoute()

export default function useShowPosts() {
    const posts_url = 'http://127.0.0.1:8000/'
    const categories_url = 'http://127.0.0.1:8000/categories/'
    const { pending, data: posts, error } = useLazyFetch(posts_url);

    // const posts = ref();
    // const err = ref();

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

    // const getCategories = async () = >{
    //     try {

    //     } catch (error) {

    //     }
    // }

    return {
        posts,
        pending,
        error,
        getPosts,
    }
}