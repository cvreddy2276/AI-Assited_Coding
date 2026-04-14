-- Library Loan System Schema and Queries
-- Using SQLite3

-- Books table
CREATE TABLE Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    isbn TEXT UNIQUE,
    published_date DATE,
    available_copies INTEGER NOT NULL DEFAULT 1 CHECK (available_copies >= 0)
);

-- Members table
CREATE TABLE Members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    membership_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Loans table
CREATE TABLE Loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE,
    status TEXT NOT NULL DEFAULT 'issued',
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (member_id) REFERENCES Members(id),
    CHECK (status IN ('issued', 'returned', 'lost'))
);

-- Indexing strategy for faster queries:
-- 1. Create an index on Loans(book_id) for book-based lookups.
-- 2. Create an index on Loans(member_id) for member history and aggregations.
-- 3. Create an index on Loans(status, loan_date) to speed up currently issued and overdue queries.
-- 4. Create an index on Books(isbn) for fast book lookup by ISBN.

CREATE INDEX idx_loans_book_id ON Loans(book_id);
CREATE INDEX idx_loans_member_id ON Loans(member_id);
CREATE INDEX idx_loans_status_loan_date ON Loans(status, loan_date);
CREATE INDEX idx_books_isbn ON Books(isbn);

-- Query 1: Retrieve all books currently issued
SELECT l.id AS loan_id,
       b.id AS book_id,
       b.title,
       b.author,
       m.id AS member_id,
       m.name AS member_name,
       l.loan_date
FROM Loans l
JOIN Books b ON l.book_id = b.id
JOIN Members m ON l.member_id = m.id
WHERE l.status = 'issued'
ORDER BY l.loan_date DESC;

-- Query 2: Find overdue books (loan date > 30 days and not returned)
SELECT l.id AS loan_id,
       b.id AS book_id,
       b.title,
       m.id AS member_id,
       m.name AS member_name,
       l.loan_date,
       julianday('now') - julianday(l.loan_date) AS days_since_loan
FROM Loans l
JOIN Books b ON l.book_id = b.id
JOIN Members m ON l.member_id = m.id
WHERE l.status = 'issued'
  AND julianday('now') - julianday(l.loan_date) > 30
ORDER BY days_since_loan DESC;

-- Query 3: Count number of books loaned by each member
SELECT m.id AS member_id,
       m.name AS member_name,
       COUNT(l.id) AS total_loans
FROM Members m
LEFT JOIN Loans l ON m.id = l.member_id
GROUP BY m.id, m.name
ORDER BY total_loans DESC;
