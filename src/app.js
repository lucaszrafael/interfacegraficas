const express = require('express');
const app = express();
const port = 5000;

/* Configurando a template engine. */
app.set('view engine', 'ejs');
app.set('views', './src/views');

/* Importando o modelo */
var { Book } = require('./models/Book');

/* Configurando o diretório que serve arquivos estáticos.*/
app.use(express.static('./src/public'));

app.get('/', homeHandler);

app.get('/search-books/:search', searchBooksHandler);

app.get('/register-book', registerBookHandler);

app.get('/update-book/:id', updateBookHandler);

app.get('/register-subject', registerSubjectHandler);

app.get('/login', loginHandler);

app.get('/recovery-search-books', recoverySearchBooksHandler);

app.listen(port, listenHandler);

function homeHandler(req, res){
    res.render('home.ejs');    
}

function searchBooksHandler(req, res){
    const search = req.params.search
    res.render('search_books.ejs', {search});    
}

function registerBookHandler(req, res){
    res.render('register_book.ejs');
}

function updateBookHandler(req, res){
    const id = req.params.id
    res.render('update_book.ejs', {id});
}

function registerSubjectHandler(req, res){
    res.render('register_subject.ejs');
}

function loginHandler(req, res){
    res.render('login.ejs');
}

function recoverySearchBooksHandler(req, res){
    let book_1 = new Book(1, "Título 1", "Assunto 1", "Autor 1", "01/06/2021"); 
    let book_2 = new Book(2, "Título 2", "Assunto 2", "Autor 2", "02/07/2022");
    let book_3 = new Book(3, "Título 3", "Assunto 3", "Autor 3", "03/08/2023");    
    let books = [];
    books.push(book_1);
    books.push(book_2);
    books.push(book_3);   
    res.render('recovery_search_books.ejs', {list_books: books});
}

function listenHandler(){
    console.log(`Escutando na porta ${port}!`);
}