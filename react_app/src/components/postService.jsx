import axios from "axios";




const axiosService = axios.create({
    baseURL: "http://localhost:8000/api/",
    timeout: 1000,
      
})

function loadAuth() {
    return JSON.parse(localStorage.getItem("auth"))
}

function getConfig(is_auth=true){
    const config = {
        headers: {"Content-Type": "application/json" },}
    if (is_auth) {
        const auth = loadAuth()
        config['Authorization'] = `Token ${auth.access}`
    }
    return config
}


const getAll = () => {
    return axiosService.get('ideas')
}

function getAuth() {
    const auth = loadAuth()
    if (auth) {
        return auth
    } else {
        return null
    }
}


function getIdea(id) {
    return axiosService.get(`idea/${id}`, getConfig())
}

function connectToIdea(id) {
    const auth = loadAuth()
    const data = { 
        idea: id,
        user: auth.id }
    return axiosService.post('join/', data, getConfig(true))
} 

function createRubric(form){
    return axiosService.post(`new_rubric/`, form, getConfig())
}

function getRubrics(){
    return axiosService.get(`rubrics/`, getConfig())
}

function postIdea(form) {
    return axiosService.post('new_idea/', form, getConfig())
}

function setInLocal(res){
    console.log("resresresresresres")
    console.log(res.user.id)
    console.log(res)
    localStorage.setItem("auth", JSON.stringify({
        access: res.access,
        refresh: res.refresh,
        login: res.user.login,
        first_name: res.user.first_name,
        last_name: res.user.last_name,
        avatar: res.user.avatar,
        email: res.user.email,
        id: res.user.id,
        age: res.user.age,
        is_superuser: res.user.is_superuser,
        }))
}

function regUser(data) {
    return axiosService.post('register/', data)
}

function logout() {localStorage.removeItem("auth")}


function logIn(data) {
    return axiosService.post('login/', data)
}

function LikeIdea(data) {
    return axiosService.post('like/', data)
}

const getAllUsers = () => {
    return axiosService.get('users')
}

function togleStatus(id, status) {
    console.log("id\n", id)
    const auth = loadAuth()
    const data = { 
        is_active: !status }
    return axiosService.patch(`users/${id}/`, data, getConfig(true))
} 

export {
    getAll,
    getAuth,
    getIdea,
    connectToIdea,
    createRubric,
    getRubrics,
    postIdea,
    loadAuth,
    logIn,
    setInLocal,
    logout,
    regUser,
    LikeIdea,
    getAllUsers,
    togleStatus,

}