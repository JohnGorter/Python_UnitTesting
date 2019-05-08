# Services

---
### Services

- fetch api
- axios 
- vue-resource 

Axios is isomorphic

---
### Using Axios 
Axios is a very popular JavaScript library for making HTTP requests
- Promise base 

Install throught NPM or through unpkg
```js
npm install axios --save
// - or -
https://unpkg.com/axios
```

Axios.get() for making GET requests
Axios.post() for sending POST requests etc

---
### Example

```js
import axios from 'axios';

<template>
  <ul v-if="todos && todos.length">
    <li v-for="todo of todos">
      <h2></h2>
    </li>
  </ul>
</template>  

export default {
  data() {
    return { todos: [] }
  },
  created() {
    axios.get('http://jsonplaceholder.typicode.com/todos')
    .then(response => { this.todos = response.data }) // <- no json call needed
    .catch(error => {
      console.log(error);
    })
  }
}
```

---
### Using vue-resource 
vue-resource is a library for Vue.js that provides an API for sending Ajax requests by wraping the JavaScript's XMLHttpRequest interface or by using JSONP

vue-resource supports
- the Promise API and URI Templates
- request's and response's interceptors
- modern browesrs such as Firefox, Chrome and Safari etc.
- both Vue.js version 1.0 and Vue.js version Vue 2.0

vue-resource was once a part of the Vue.js library, but was retired in Vue 2.0
The project is still maintained and used by the community

---
### Install vue-resource
Install through npm:
```js
npm install vue-resource --save
- or -
https://unpkg.com/vue-resource
```

Configuration is needed by calling the global method Vue.use() to use the plugin

---
### Example
First configure it

```js
/* ... */
Vue.use(VueResource);
/* ... */
new Vue({  el: '#app', render: h => h(App) })
```
Then use it
```js
...
mounted() {
    this.$http.get("http://jsonplaceholder.typicode.com/todos").then(response => {
        this.todos = response.body;
    }, error => {  console.error(error);  });
}
```

* to send a POST request, use this.$http.post()

---
###  Using the browser's fetch API 
Modern browsers have an API designed specifically for making AJAX requests or HTTP callscalled fetch.

```js
fetch("http://jsonplaceholder.typicode.com/todos").then(function (response) {
            return response.json();
    }).then(function (result) {
        this.todos =  result;   
    });
```

The modern fetch API is much cleaner and easier to use than XMLHttpRequest

---
###  Using the browser's fetch API (2)
You can also do POST, PUT and DELETE calls by providing an options parameter:
```js
fetch('https://jsonplaceholder.typicode.com/todos', {
        method: 'POST',
        body:JSON.stringify({title:"a new todo"})
}).then((res) => res.json())
.then((data) =>  console.log(data))
.catch((err)=>console.error(err))
```

This is a simple example of using fetch. For more information and in depth look at the API, you can see Introduction to Fetch.

---
### Wrapping Up
There are many ways to work with Vue and axios beyond consuming and displaying an API
You can also communicate with 
- Serverless Functions 
- post/edit/delete from an API where you have write access


---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Calling Services

---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Getting the data from the server