import React, { useEffect, useState } from "react"
import Filter from './Filter'
import Idea from "./Idea";
import axios from "axios";


function Main() {
    const [ideas, setIdeas] = useState([])

    useEffect(() => {
        const ideas = axios.get('http://127.0.0.1:8000/api/ideas/')
        ideas.then( res => {
            console.log(res.data)
            setIdeas(res.data.results)
        })
        .catch(err => {
            console.log(err)}
        )
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
                            preview={idea.preview}/>
                        </div>
                    )};
                </div>
            </div>
        </div>
        ) 
}
export default Main