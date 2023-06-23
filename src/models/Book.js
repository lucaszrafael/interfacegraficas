class Book {

    constructor(id, title, subject, author, publication_date){
        this.id = id;
        this.title = title;
        this.subject = subject;
        this.author = author;
        this.publication_date = publication_date;
    }
    
}

module.exports = { Book }