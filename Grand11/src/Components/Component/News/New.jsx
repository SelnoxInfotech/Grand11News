import { React, useContext, useState, useEffect } from 'react'
import parse from 'html-react-parser';
import news from "../../context/NewsApi";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";

export default function New() {
    const imagePerRow = 3
    const [match_new, set_matche_new] = useState([]);
    const [next, setNext] = useState(imagePerRow);
    const data1 = useContext(news);

    const handleMoreImage = () => {
        setNext(next + imagePerRow);
    };
    const handlelessImage = () => {
        setNext(next - imagePerRow);
    };
    useEffect(() => {
        set_matche_new(data1.news)
    }, [data1])
    return (
        <section id="team" className="pb-5">
            <Helmet>
                <title>Latest Cricket News | G11 Fantasy Cricket Prediction </title>
                <meta name="viewport" content="initial-scale=1.0, width=device-width" />
                <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
                <meta name="description" key="description" content="Latest Cricket News on Trending topics. G11 Fantasy Cricket Prediction Website and Application for Today's match. # 1 Dream11 Fantasy Cricket Prediction tips"></meta>
                <meta property="og:locale" key="og:locale" content="en_US" />
                <meta charSet="utf-8" />
                <meta property="og:type" key="og:type" content="website" />
                <meta
                    property="og:description"
                    key="og:description"
                    content={"Latest Cricket News on Trending topics. G11 Fantasy Cricket Prediction Website and Application for Today's match. # 1 Dream11 Fantasy Cricket Prediction tips"}
                />
                <meta
                    property="og:image"
                    key="og:image"
                    content={`/images/G11.png`}
                />
            </Helmet>
            <div className="container">
                <h1 className="section-title ">Latest Cricket News ON TRENDING TOPICS</h1>
                <div className="row" id="team_data" >
                    {
                        match_new?.slice(0, next)?.map((data, index) => {
                            return (

                                <div className="col-xs-12 col-sm-6 col-md-4" key={index}>
                                    <div className="image-flip" >
                                        <div className="mainflip flip-0">
                                            <div className="frontside">
                                                <div className="card">
                                                    <div className="card-body text-center">
                                                        <span><img className=" img-fluid" src={`https://grand11.in/g11/${data.image}`} alt="news_image" /></span>
                                                        <div>
                                                            <p className="card-text content col_card_heading">{data.title}</p>
                                                        </div>
                                                        <span >{data.post_date}</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="backside">
                                                <div className="card">
                                                    <div className="card-body text-center mt-4">
                                                        <span className="card-text ">{parse(data.content.substr(0, 400))}</span>
                                                        <Link to={`/Cricket-News/${data.id}/${data.title.replace(/\s+/g, '-')}`}><button className='hovereffect btn primary'/* onClick={() => {handleClickSlide(data.id) }}*/>Read More</button></Link>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            )
                        })
                    }
                </div>
                <div className='row'>
                    <div className='col-12 center '>
                        {next < match_new?.length && (
                            <button className="btn readleft" onClick={handleMoreImage}
                            >
                                Load more
                            </button>
                        )}
                        {next < match_new?.length && (
                            <button className={next <= 3 ? 'hidden' : "btn readleft"} onClick={handlelessImage}
                            >
                                Read Less
                            </button>
                        )}
                    </div>

                </div>
            </div>
        </section>

    )
}




























































