import React, { useEffect, useState } from "react"
import Filter from './Filter'
import Idea from "./Idea";
import {useUserActions} from "../API/useUserActions";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Main() {
    const [ideas, setIdeas] = useState([])

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/ideas/")
        
        .then({res} => return (
            console.log(res),
            setIdeas(res.data.results)))
      }, [setIdeas]);


    if (ideas.length === 0) {return <div>Нет идей</div> }
    
    return (
        <div className="container-md mt-5 idea-list">
            <div className="row justify-content-center align-items-top">
                <Filter val={ideas}/>
                <div className="col">
                    {ideas.map(idea =>
                        <div className="page">
                            <Idea 
                                key={idea.preview}
                                autor={idea.autor}
                                title={idea.title}
                                rubrics={idea.rubrics}
                                body={idea.body}
                                preview={idea.preview}
                            />
                        </div>
                    )};
                </div>
            </div>
        </div>
        ) 
}
export default Main