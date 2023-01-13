import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { CiCalendarDate } from 'react-icons/ci';
import Slider from "react-slick";
import { Link } from 'react-router-dom';

export default function BreakingNewsList() {
    const settings = {
        dots: true,
        // infinite: true,
        // slidesToShow: 4,
        slidesToScroll: 1,
        vertical: true,
        verticalSwiping: true,
        beforeChange: function (currentSlide, nextSlide) {
            
        },
        afterChange: function (currentSlide) {
           
        }
    };

    const [breakingnews, setbreakingnews] = useState([])
    useEffect(() => {
        axios("https://www.g11fantasy.com/NewsSection/Get-News/", {
            method: 'GET',

        }).then(response => {
            if (response.status === 200) {
                setbreakingnews(response.data)

            }
        })
    }, [])

    window.scrollTo(0, 0);

    return (
        <div className='container-fluid'>
            <div className='row'>
                <div className='col-12  breaking_news_hed '>
                    <h1> Cricket Breaking News ON TRENDING TOPICS</h1>
                </div>
                <Slider {...settings}  >
                    <div style={{ display: "flex" }} className="slider_breaking">

                        {
                            breakingnews.map((breakingnews, index) => {
                                return (
                                    <Link to={`/Cricket-BreakingNews/${breakingnews.id}/${breakingnews.Title.replace(/\s+/g, '-')}`} key={index}>
                                        <div className='col-12 breakingcard' >
                                            <div className='col card1'>

                                                <img src={`https://www.g11fantasy.com${breakingnews.Image} `} alt={breakingnews.Alt_Text} className="card_image_breaking" />

                                            </div>
                                            <div className='col-10'>

                                                <p className='card_title'>
                                                    {breakingnews.Title}
                                                </p>
                                                <p className='card_time_breaking'>
                                                    <span className="ClenderIcon"> <CiCalendarDate></CiCalendarDate></span>
                                                    <span>  {breakingnews.updated.slice(0, 10)}</span>
                                                </p>
                                            </div>
                                        </div>
                                    </Link>

                                )
                            })

                        }
                    </div>
                </Slider>
            </div>
        </div>
    )
}
