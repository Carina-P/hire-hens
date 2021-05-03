# TEST

Back to [README](https://github.com/Carina-P/ms3-best-books/blob/master/README.md)

## Contents

## Test plan
The below plan for testing was followed during development of the site:
The TDD, **TestDriven Development**, process is followed as much as possible. 
Test cases are developed/thought off, before the code is implemented. The test
process is conducted in an iterative manner and implementation cycles are short
with small code parts every time. In some cases, **prototyping** is used and
the thorough test is done when satisfied with the prototype.

Before new code is committed, testing of all code developed earlier are
repeated again.

When all features are implemented and tested, the following tests are 
performed:
- Go through the test cases for functional testing and testing of
responsiveness, as described below
- **HTML-code validated** by 
[W3S Markup validation service](https://validator.w3.org/)
- **CSS-cod validated** by 
[W3S CSS validation service](https://jigsaw.w3.org/css-validator/)
- **JavaScript-code validated** by [JSHint](https://jshint.com/)
- **Python** code is **validated** by [PEP8](https://pypi.org/project/pep8/) 
- The site is tested on **different browsers**, as described below
- The **deployed version** in heroku is tested

## Tests of functionality and responsiveness
Functionality tests and tests of responsiveness are done by following test cases
below.
Test of responsiveness is mainly performed with help of Chrome Developers Tool. 
The site is also tested with iPad mini and iPhone8.

### Test cases
Test cases are described below and linked to use cases. Each test case have
a name beginning with TC and then a number, for example TC_001.

When testing: Please **start with** testcases **TC_015, TC016, TC017 and TC020**

- Testing use case **US_001**. As a user I want to browse for a book:

    **TC_001** Browse for a book by giving the books title:
    - How to test:
        - Go to homepage and look for the header: "Search for book in this databas" or
        Use navigation bar and choose "Search for book"
        - Print "Where the Crawdads Sing" in the field
        - Press return
    - Expected outcome:
        - View is moved to the "Search results" page.
        - The book is found there. Or message that book is not present in site.
        - Check that information in database corresponds to the result in the page.

#### Test protocol
The outcome of testing according to above test cases is documented in [Test Protocol](https://github.com/Carina-P/ms3-best-books/blob/master/test/protocol_test_cases.pdf).


## UX testing
UX testing is **conducted by watching and interviewing users** when they used
the page. Examples of issues/discussions:

## Code validation
### Validation with W3S
- **HTML**: Validated with **no errors** or warnings. Notice! Some headers are filled from JavaScript, if
code is validated when the JavaScript has not been run, you will get warnings about empty headers. That 
applies to code belonging to Add Book and also for Modals.
    - In GitHub the template: form_add_book.html, is marked as it has an error. The code is working as
    I want it to and I cannot find any problem. I talked to Code Institutes Tutore, and they told me
    "The code is fine but validators don't want to read JavaScript functionality on a HTML page in the body content."
- **CSS**: Validated with **no errors** or warnings.

### Validation with JSHint
**JavaScript** validated with **no errors**. 
- There are **one undefined variables**: 
    - $ (JQuery)
- There are **seven unused variables**:
    - moveTo, cancelAddBook, addBook, searchBooks, addOpinion, changeOpinion and buyBook:
    These are all functions called from HTML.

### Validation with PEP8
PEP8 was included in the IDE and thus the **python** code is validated within GitHub.
Validation without errors or warnings.

## Different browsers
The code is **mainly tested with Chrome**. But also **Firefox and Safari**.
- According to [W3 Schools](https://www.w3schools.com/js/js_es6.asp) the 
**JavaScript** code will probably not work well on browsers less than the 
following versions: **Chrome 58, Edge 14, Firefox 54, Safari 10 and Opera 55**. 
That are because following features from **ECMAScriptS6** is used: 
    - let
    - template literal syntax
    - arrow function
- **Bootstrap 4** is used and according to [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/browsers-devices/)
you need at least: 
**Chrome 45, Firefox 38, Edge 12, IE10, iOS 9, Safari 9, Android 4.4 and Opera 30**.
- **HTML5 semantics and form features** are used, according to [Can I use](https://caniuse.com/?search=HTML5), that requires at least:
**IE9, Firefox 4, Safari 4 and Android Browser 4.4**. **Opera mini** cannot be used.
    

## Some of the bugs

## Remaining bugs