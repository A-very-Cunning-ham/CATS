//Express server setup
const express = require('express')
// app.use(express.urlencoded())
//Multer Image upload package
const multer  = require('multer')
//Express Setup
const app = express()
const port = 3000
app.use(express.json())
//Save to disk setup
let filepath = 'C:/Users/brado/AppData/Local/Temp/express-uploads'
const fs = require("fs");
fs.mkdirSync(filepath, { recursive: true })

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, filepath)
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9)
    cb(null, file.fieldname + '-' + uniqueSuffix)
  }
})

const upload = multer({ storage: storage, limits: {fileSize: 1024 * 1024 * 15} })


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/postImage', upload.single("catImage"), function (req, res) {
  console.log(req)
  console.log(req.body)
  console.log(`req.body: ${JSON.stringify(req.body)}`)
  console.log(`req.file: ${req.file}`)
  console.log(`req.body.time: ${req.body.time}`)
  console.log(`req.body.location: ${req.body.location}`)
  res.send(200)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})