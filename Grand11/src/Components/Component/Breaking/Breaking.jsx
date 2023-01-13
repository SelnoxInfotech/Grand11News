import React, { useState, useEffect } from "react";
import axios from "axios";
import parse from 'html-react-parser';
import { useParams } from "react-router-dom";
import BreakingNewsList from "./BreakingNewsList";
export default function Breaking() {
    const {id} = useParams();
    const [breakingnews, setbreakingnews] = useState([])
    useEffect(() => {
        axios(`https://www.g11fantasy.com/NewsSection/Get-Newsbyid/${id}`, {
            method: 'GET',

        }).then(response => {
            if (response.status === 200) {
                setbreakingnews(response.data.data)

            }
        })
    }, [id])



    return (
        <div>{
            breakingnews.map((data,index) => {
                return (
                
                        
                            <div className="container "  >
                               <div className="row">
                                <div className="col-12"> <h1 className="title_had">{parse(data.Title)}</h1></div>
                                <div className="col-12 imag">
                                {parse(data.Description)}
                                </div>
                               </div>
                            </div>
                        
                    
                )
            })

        }
        <BreakingNewsList></BreakingNewsList>
        </div>
    )
}
