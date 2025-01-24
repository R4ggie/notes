<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: 'Jersey 15', sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --secondary-color: #f1d6ab;
  --primary-color: #e3b04b;
  --light-color: #f8f8f8;
  --dark-color: #2b2b28;
  --dark-text: #191918;
}

body {
  font-family: 'Jersey 15', sans-serif;
  font-size: 20px;
  color: #191918;
  line-height: 1.5;
  background: #fff;
}

a {
  text-decoration: none;
  color: var(--light-color);
}

ul {
  list-style: none;
}

img {
  max-width: 100%;
}

table {
  border: none;
  width: 100%;
  padding: 20px;
  color: var(--dark-text);
}

th {
  text-align: center;
  background-color: var(--primary-color);
  padding: 8px;
}

td {
  text-align: center;
  background-color: var(--secondary-color);
  padding: 8px;
}

tr {
  text-align: center;
  background-color: var(--secondary-color);
  padding: 8px;
}

button {
  font-size: 1.2rem;
  font-family: 'Jersey 15', sans-serif;
  border-radius: 4px;
  border: none;
  background-color: var(--light-color);
  padding: 10px;
  text-align: center;
}

button:hover {
  background-color: var(--primary-color);
  color: #191918;
  transition-duration: 0.2s;
}

button:active {
  transform: translateY(4px);
}

.font-light {
  color: var(--light-color);
}
.font-dark {
  color: var(--dark-text);
}

.center {
  margin: auto;
  width: 60%;
  padding: 10px;
}

.middle {
  display: grid;
  place-items: center;
  padding: 20px;
}

.dark-bg {
  background: var(--dark-color);
}

.container {
  padding: 30px;
  display: flex;
  justify-content: center;
}

.btn-tb {
  background-color: var(--dark-text);
  color: var(--primary-color);
  border-radius: 4px;
}

.btn-cls {
  background-color: var(--light-color);
  color: var(--primary-color);
  border-radius: 4px;
}
</style>
