const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://covers.openlibrary.org/b/id/7984916-L.jpg",
    alreadyRead: true
  },
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://covers.openlibrary.org/b/id/6979861-L.jpg",
    alreadyRead: false
  }
];

const bookSection = document.querySelector(".listBooks");

for (let book of allBooks) {
  const bookDiv = document.createElement("div");

  const bookInfo = document.createElement("p");
  bookInfo.textContent = `${book.title} written by ${book.author}`;
 
  const bookImg = document.createElement("img");
  bookImg.src = book.image;
  bookImg.width = 100;

  if (book.alreadyRead) {
    bookInfo.style.color = "red";
  }
  
  bookDiv.appendChild(bookInfo);
  bookDiv.appendChild(bookImg);
  bookSection.appendChild(bookDiv);
}