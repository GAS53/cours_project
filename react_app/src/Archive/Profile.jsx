import React from "react";
import { useParams } from "react-router-dom";
import Layout from "../components/Layout";
// import ProfileDetails from "../components/profile/ProfileDetails";
// import useSWR from "swr";
// import { fetcher } from "../helpers/axios";
// import { Post } from "../components/posts";
// import { Row, Col } from "react-bootstrap";
import useUserActions from "../API/useUserActions";


function Profile() {
    const { profileId } = useParams();
    // const user = useSWR(`/user/${profileId}/`, fetcher);
    // const posts = useSWR(`/post/?author__public_id=${profileId}`, fetcher, {refreshInterval: 20000});
    const userActions = useUserActions();
    // const { toaster, setToaster } = useContext(Context);
    // const { profileId } = useParams();
    // const user = 
    // const test = userActions.edit( profileId)
    axios.post('http://127.0.0.1:8000/api/login/', data)
        .then((res) => {
            localStorage.setItem("auth", JSON.stringify({
            access: res.data.access,
            refresh: res.data.refresh,
            user: res.data.user,
            email: data.email,
            password: data.password,
            id: res.data.id,
            }));
            navigate("/");
            console.log('login')
            console.log(res)}
            )
        .catch((err) => {
                if (err.message) {setError(err.request.response);}
                });
            }