
<a name="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/Econvert">
    <img src="https://i.imgur.com/ihu3AoY.png" alt="Logo" width="400" height="400">
  </a>

<h3 align="center">Econvert</h3>

  <p align="center">
All-In-One Currency Converter
    <br />
    <a href="https://github.com/aleguzmancs9/Econvert.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Our web application, Econvert, is a web-based tool that allows the user to select any currency (euros, mexican pesos, pounds, yen, etc), any ancient currencies (shekels, romanian currency, silver coins, etc), and even in-game currencies (vbucks, robux, rocket league credits, etc). The application frontend and backend is managed all in Python, by importing the Reflex API to create our starting HTML, CSS, and JavaScript template. Our backend is run on Reflex to allow our Python code to be converted into JavaScript and we also implement the Together AI API to work as our currency converter. Our site takes in two inputs from the user, the currency they want the usd amount to be converted into, and the amount of money (usd). Our AI then returns the conversion amount and it is displayed to the user in a chatbot type format.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Reflex][Reflex-url]
* [Together.ai][Together-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* reflex
  ```sh
  pip install reflex
  ```
* Together.ai
  ```sh
  pip install together
  ```

### Installation

1. Get a free API Key at [https://together.ai/apis](https://together.ai/apis)
2. Import packages
   ```sh
   import reflex as rx
   ```
   ```sh
   import together
   ```
3. Enter your API in `terminal`
   ```bash
   export TOGETHEI_API_KEY='Enter Your Api'
   ```
4. Enter your API in `reflex`
   ```reflex
   together.api_key = "Enter Your Api"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

<div style="display: flex;">
  <img src="https://i.imgur.com/T6J1cd4.png" alt="Example1" width="200" style="margin-right: 20px;" />
  <img src="https://i.imgur.com/lgdHmGq.png" alt="Example2" width="200" />
</div>





<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Alexis Guzman - [Linkedin](linkedin.com/in/alexis-guzman-cs9) - aleguzmancs9@gmail.com
Sergio Zavala - [Linkedin](linkedin.com/in/sergiozavala1) - sezavala@csumb.edu

Project Link: [https://github.com/aleguzmancs9/Econvert.git](https://github.com/aleguzmancs9/Econvert.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: linkedin.com/in/alexis-guzman-cs9
[product-screenshot]: images/screenshot.png
[Reflex.dev]: https://reflex.dev/Reflex.svg
[Reflex-url]: https://reflex.dev/
[Together.ai]: https://images.squarespace-cdn.com/content/v1/6358bea282189a0adf57fe16/f0f7f485-91ef-47f6-b67c-305c10d73b59/together.ai+logo.png?format=1500w
[Together-url]: https://together.ai/
