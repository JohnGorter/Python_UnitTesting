# Setup

---
### Getting started

What you need:
* Nothing Really :-)

What you need to know:
* HTML
* JavaScript / ES6

---
### How to include VueJS
You can load them on the fly from a CDN (great for prototyping, bad for performance).

Or...

Use Webpack to create a development workflow with hot-reloading, unit testing and minification.

Hint: this has been done by others, too!

---
### Using the Vue CLI
To install 
```js
npm i -g @vue/cli
```
Type vue to get help 
```js
vue 
```

---
### USe Vue CLI
To create a new project
```js
vue create sample
```
to start the project
```js
cd sample
yarn serve
```
other yarn scripts
```js
yarn build | lint | test:unit
```

---
### Rapid prototyping
install
```js
npm install -g @vue/cli-service-global
yarn global add  @vue/cli-service-global
```
create a component
```js
<template><h1>Hello world</h1></template>
```
run
```js
vue serve app.vue
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Using Vue Cli


---
### Use Vue UI
A user interface / browser tool to 
- scaffold a new app
- Install plugins
- List dependencies
- Modify configurations
- Specify tasks
    - Serve - Compiles and hot reloads your application
    - Build - Compiles and minifies for production
    - Lint - Lints and fixes files
    - Test - Run tests using Mocha
    - Inspect - inspect the resolved webpack config
- Serve the application

https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-ui

---
### Vue UI Dashboard
The dashboard tab shows various stats about your application bundle, you can inspect it to see file sizes, and even loading speeds for your files.

<img src="/images/dashboard.webp" style="height:40vh">



---
### Analyzer
The analyzer tab, tries to analyze your code, and create a graph showing the various dependencies of your code
- purple part representing the code we have written
- green section represents the code that we imported from dependencies

<img src="/images/analyser.webp" style="height:40vh">

---
### Build
The build section has the almost similar to the serve section, only that it produces a production bundle that can be used to deploy the application

<img src="/images/build.webp" style="height:10vh">

---
### Lint
Lint should be straight forward. It will lint your code and give you an output
<img src="/images/lint.webp" style="height:40vh">

---
### Unit test

This will allow us to run unit tests for our application
We just click on Run task, and see the output 

<img src="/images/unittest.webp" style="height:40vh">

---
### Inspect
This will produce the configuration of your webpack, in a json file

<img src="/images/inspect.webp" style="height:40vh">

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Using Vue UI

---
###  VueJS Devtools
Vue has a great panel that integrates into the Browser Developer Tools, which lets you inspect your application and interact with it, to ease debugging and understanding

Can be installed:
- on Chrome
- on Firefox
- as a standalone app

---
###  Use the Devtools
You can use the devtools to 
- Filter components
- Select component in the page
- Format components names
- Filter inspected data
- Inspect DOM
- Show emitted events

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Using Vue DevTools

---
###  VueJS in VSCode
Interesting plugin
- Vetur
    - Syntax highlighting
    - Snippets
    - Intellisense
    - Scaffolding
    - Emmet
    - Linting and error checking
    - Code formatting

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Installing and using Vetur

---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Setting up the tools



