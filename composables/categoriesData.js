import { ref } from 'vue'
// import axios from 'axios';

// const route = useRoute()

export default function useCategoryPosts(url = 'http://127.0.0.1:8000/categories/', parameter = '', id = null) {
    // const categories_url = 'http://127.0.0.1:8000/categories/'
    const { pending: pendings, data: categories, error: errors } = useLazyFetch(url);
    // const categories_url = 'http://127.0.0.1:8000/categories/'
    // const { pending: pendings, data: categories, error: errors } = useLazyFetch(categories_url);
    // const categories = ref();
    // const pendings = ref();
    // const errors = ref();
    // const categoriesCategory = ref();
    // const url = ref('');


    const getCategories = async () => {

        // const { pending: pendings, data: categories, error: errors } = useLazyFetch(categories_url);

        try {
            // const res = await axios(url)
            console.log('categories are here', categories);
            // categories
        } catch (error) {
            console.log('categories errors are here', errors);
            // error
        }
    }

    const { pending: pending, data: categoriesCategory, error: error } = useLazyFetch(url);

    const getCategoriesCategory = async () => {

        try {
            console.log('categories Category are here', categoriesCategory);
        } catch (error) {
            console.log('categories Category errors are here', error);
        }
    }

    const { pending: pending_data, data: category, error: error_data } = useLazyFetch(url);

    const getCategory = async () => {

        try {
            console.log('Category is here', category);
        } catch (error_data) {
            console.log('Category error_data is here', error_data);
        }
    }


    return {
        // all about categories 
        categories,
        pendings,
        errors,
        getCategories,
        // Categories category all about 
        pending,
        error,
        categoriesCategory,
        getCategoriesCategory,
        // Single Category is here 
        pending_data,
        error_data,
        category,
        getCategory
    }
}