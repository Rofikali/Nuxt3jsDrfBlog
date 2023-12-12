// import { Ref } from "vue";

import { ref } from 'vue'
import axios from 'axios'

export default function useStudent() {
    const url = "http://localhost:8000/"
    const postsData = ref([])
    const error = ref(null)
    const statusCode = ref(null)
    const delError = ref(null)
    // Get All Students Data
    const getAllStudent = async () => {
        studentData.value = []
        error.value = null
        try {
            const res = await axios(url)
            // console.log(res.data)
            studentData.value = res.data
        } catch (err) {
            // console.log(err)
            error.value = err
        }
    }
}