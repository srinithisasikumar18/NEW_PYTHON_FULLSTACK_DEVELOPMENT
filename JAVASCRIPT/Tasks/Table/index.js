// Get reference to the table body
let tbody = document.querySelector("#table1 tbody");

// Sample data (you can later get this from user input, API, etc.)
let employees = [{ "eid": 1, "name": "Eden", "email": "evamplew0@dmoz.org", "gender": "Female" },
{ "eid": 2, "name": "Sammy", "email": "sgimeno1@ted.com", "gender": "Female" },
{ "eid": 3, "name": "Louise", "email": "lskryne2@issuu.com", "gender": "Female" },
{ "eid": 4, "name": "Novelia", "email": "narnet3@howstuffworks.com", "gender": "Female" },
{ "eid": 5, "name": "Otha", "email": "otaw4@intel.com", "gender": "Agender" },
{ "eid": 6, "name": "Alisun", "email": "agroombridge5@facebook.com", "gender": "Agender" },
{ "eid": 7, "name": "Antonius", "email": "ahessel6@smh.com.au", "gender": "Male" },
{ "eid": 8, "name": "Marcelle", "email": "mcoale7@baidu.com", "gender": "Female" },
{ "eid": 9, "name": "Gaylor", "email": "gpietrasik8@yahoo.com", "gender": "Non-binary" },
{ "eid": 10, "name": "Sallyann", "email": "sjopke9@fastcompany.com", "gender": "Female" },
{ "eid": 11, "name": "Bradford", "email": "bedmeda@twitpic.com", "gender": "Male" },
{ "eid": 12, "name": "Dannel", "email": "dbeckworthb@mysql.com", "gender": "Male" },
{ "eid": 13, "name": "Persis", "email": "psweetc@reuters.com", "gender": "Female" },
{ "eid": 14, "name": "Gina", "email": "gcruxtond@ning.com", "gender": "Female" },
{ "eid": 15, "name": "Godwin", "email": "gbulbecke@imdb.com", "gender": "Male" },
{ "eid": 16, "name": "Filbert", "email": "fgostlingf@diigo.com", "gender": "Agender" },
{ "eid": 17, "name": "Agustin", "email": "agerrettg@china.com.cn", "gender": "Male" },
{ "eid": 18, "name": "Paddie", "email": "pgrimwoodh@marriott.com", "gender": "Male" },
{ "eid": 19, "name": "Roselia", "email": "rmumbrayi@latimes.com", "gender": "Female" },
{ "eid": 20, "name": "Jocelin", "email": "jfarendenj@si.edu", "gender": "Genderqueer" },
{ "eid": 21, "name": "Sidonnie", "email": "strayfordk@flickr.com", "gender": "Female" },
{ "eid": 22, "name": "Marrissa", "email": "mcantillonl@adobe.com", "gender": "Genderqueer" },
{ "eid": 23, "name": "Cullan", "email": "clavallm@tuttocitta.it", "gender": "Male" },
{ "eid": 24, "name": "Adrea", "email": "atoulchn@wp.com", "gender": "Female" },
{ "eid": 25, "name": "Whittaker", "email": "wlayneo@dell.com", "gender": "Male" },
{ "eid": 26, "name": "Patrica", "email": "phargrevesp@slashdot.org", "gender": "Female" },
{ "eid": 27, "name": "Sybilla", "email": "sdoddrellq@1688.com", "gender": "Female" },
{ "eid": 28, "name": "Kassie", "email": "kbarokr@com.com", "gender": "Bigender" },
{ "eid": 29, "name": "Arluene", "email": "azanassis@mediafire.com", "gender": "Female" },
{ "eid": 30, "name": "Steve", "email": "speasegoodt@wisc.edu", "gender": "Male" },
{ "eid": 31, "name": "Derk", "email": "dmccaughanu@dyndns.org", "gender": "Male" },
{ "eid": 32, "name": "Harriett", "email": "hfransemaiv@hhs.gov", "gender": "Female" },
{ "eid": 33, "name": "Elke", "email": "ekopmanw@purevolume.com", "gender": "Female" },
{ "eid": 34, "name": "Laurens", "email": "ljerchex@sfgate.com", "gender": "Male" },
{ "eid": 35, "name": "Broderick", "email": "bambrogioniy@sbwire.com", "gender": "Male" },
{ "eid": 36, "name": "Garrett", "email": "ghubbucksz@npr.org", "gender": "Male" },
{ "eid": 37, "name": "Florinda", "email": "fgilfether10@barnesandnoble.com", "gender": "Agender" },
{ "eid": 38, "name": "Levy", "email": "lflobert11@cafepress.com", "gender": "Male" },
{ "eid": 39, "name": "Peri", "email": "ptremain12@quantcast.com", "gender": "Female" },
{ "eid": 40, "name": "Sarette", "email": "sserrell13@blogspot.com", "gender": "Female" },
{ "eid": 41, "name": "Imogen", "email": "imorby14@prweb.com", "gender": "Agender" },
{ "eid": 42, "name": "Sherm", "email": "sbirchner15@wordpress.org", "gender": "Male" },
{ "eid": 43, "name": "Kimberley", "email": "kbyfford16@yelp.com", "gender": "Female" },
{ "eid": 44, "name": "Lucias", "email": "ldadge17@epa.gov", "gender": "Male" },
{ "eid": 45, "name": "Pat", "email": "pfaustin18@dot.gov", "gender": "Female" },
{ "eid": 46, "name": "Michele", "email": "mmoiser19@prlog.org", "gender": "Male" },
{ "eid": 47, "name": "Mercy", "email": "mclemoes1a@cnn.com", "gender": "Female" },
{ "eid": 48, "name": "Christoffer", "email": "cjiggens1b@goo.gl", "gender": "Male" },
{ "eid": 49, "name": "Pearle", "email": "pblodg1c@cnet.com", "gender": "Female" },
{ "eid": 50, "name": "Kip", "email": "kassante1d@omniture.com", "gender": "Genderqueer" },
{ "eid": 51, "name": "Arlen", "email": "astorah1e@mac.com", "gender": "Female" },
{ "eid": 52, "name": "Misty", "email": "mcastiglione1f@tinypic.com", "gender": "Female" },
{ "eid": 53, "name": "Elisabet", "email": "ebloxham1g@mac.com", "gender": "Female" },
{ "eid": 54, "name": "Jason", "email": "jrosario1h@hao123.com", "gender": "Male" },
{ "eid": 55, "name": "Dori", "email": "dmallender1i@amazonaws.com", "gender": "Female" },
{ "eid": 56, "name": "Moria", "email": "mantonignetti1j@oaic.gov.au", "gender": "Female" },
{ "eid": 57, "name": "Mendel", "email": "msansum1k@hatena.ne.jp", "gender": "Male" },
{ "eid": 58, "name": "Horatius", "email": "hhodgins1l@si.edu", "gender": "Male" },
{ "eid": 59, "name": "Zulema", "email": "zdoumenc1m@amazonaws.com", "gender": "Female" },
{ "eid": 60, "name": "Tannie", "email": "tsaulter1n@hexun.com", "gender": "Male" },
{ "eid": 61, "name": "Hussein", "email": "hbudd1o@earthlink.net", "gender": "Male" },
{ "eid": 62, "name": "Isiahi", "email": "icrossan1p@cdc.gov", "gender": "Male" },
{ "eid": 63, "name": "Nowell", "email": "nbrideau1q@over-blog.com", "gender": "Male" },
{ "eid": 64, "name": "Cammy", "email": "clambirth1r@mtv.com", "gender": "Male" },
{ "eid": 65, "name": "Alasdair", "email": "adripp1s@cbslocal.com", "gender": "Male" },
{ "eid": 66, "name": "Cosimo", "email": "cpeiser1t@yelp.com", "gender": "Male" },
{ "eid": 67, "name": "Lory", "email": "lflobert1u@wired.com", "gender": "Female" },
{ "eid": 68, "name": "Robinetta", "email": "rcuddihy1v@icio.us", "gender": "Female" },
{ "eid": 69, "name": "Cordie", "email": "cjoynes1w@dagondesign.com", "gender": "Female" },
{ "eid": 70, "name": "Alva", "email": "ascroyton1x@engadget.com", "gender": "Male" },
{ "eid": 71, "name": "Robbie", "email": "rvasentsov1y@furl.net", "gender": "Male" },
{ "eid": 72, "name": "Elihu", "email": "edomney1z@macromedia.com", "gender": "Male" },
{ "eid": 73, "name": "Miquela", "email": "mgilleson20@netscape.com", "gender": "Female" },
{ "eid": 74, "name": "Hastie", "email": "hram21@biblegateway.com", "gender": "Agender" },
{ "eid": 75, "name": "Lydia", "email": "lswyersexey22@technorati.com", "gender": "Female" },
{ "eid": 76, "name": "Abby", "email": "abarabisch23@mlb.com", "gender": "Female" },
{ "eid": 77, "name": "Sile", "email": "sbeamond24@japanpost.jp", "gender": "Female" },
{ "eid": 78, "name": "Gav", "email": "glockyear25@jimdo.com", "gender": "Male" },
{ "eid": 79, "name": "Mavis", "email": "mmitskevich26@surveymonkey.com", "gender": "Female" },
{ "eid": 80, "name": "Demetri", "email": "dmalloch27@samsung.com", "gender": "Male" },
{ "eid": 81, "name": "Katina", "email": "kknott28@msn.com", "gender": "Female" },
{ "eid": 82, "name": "Llewellyn", "email": "lhutchence29@pen.io", "gender": "Male" },
{ "eid": 83, "name": "Webster", "email": "wburkman2a@apple.com", "gender": "Male" },
{ "eid": 84, "name": "Mufi", "email": "mhadwin2b@kickstarter.com", "gender": "Female" },
{ "eid": 85, "name": "Alessandro", "email": "acollingdon2c@princeton.edu", "gender": "Male" },
{ "eid": 86, "name": "Woodie", "email": "wpeepall2d@amazonaws.com", "gender": "Male" },
{ "eid": 87, "name": "Aldis", "email": "alighten2e@google.fr", "gender": "Male" },
{ "eid": 88, "name": "Broderic", "email": "bgeraldini2f@theglobeandmail.com", "gender": "Male" },
{ "eid": 89, "name": "Izak", "email": "iwaiting2g@xing.com", "gender": "Male" },
{ "eid": 90, "name": "Reidar", "email": "rmccarroll2h@gnu.org", "gender": "Male" },
{ "eid": 91, "name": "Martha", "email": "mshallcrass2i@amazon.co.uk", "gender": "Female" },
{ "eid": 92, "name": "Izaak", "email": "imacinherney2j@soup.io", "gender": "Male" },
{ "eid": 93, "name": "Kit", "email": "kballance2k@fastcompany.com", "gender": "Male" },
{ "eid": 94, "name": "Bale", "email": "bocullinane2l@biglobe.ne.jp", "gender": "Male" },
{ "eid": 95, "name": "Reggie", "email": "rakett2m@msu.edu", "gender": "Male" },
{ "eid": 96, "name": "Holli", "email": "henglishby2n@behance.net", "gender": "Female" },
{ "eid": 97, "name": "Mallorie", "email": "mmourant2o@comsenz.com", "gender": "Female" },
{ "eid": 98, "name": "Roth", "email": "rdimitru2p@earthlink.net", "gender": "Male" },
{ "eid": 99, "name": "Berry", "email": "bsilversmidt2q@washington.edu", "gender": "Female" },
{ "eid": 100, "name": "Kristine", "email": "kgoing2r@stumbleupon.com", "gender": "Female" }]

// Loop through array and add rows
employees.forEach(emp => {
    let row = document.createElement("tr");

    // Create and append table data cells
    let cell1 = document.createElement("td");
    cell1.textContent = emp.eid;
    row.appendChild(cell1);

    let cell2 = document.createElement("td");
    cell2.textContent = emp.name;
    row.appendChild(cell2);

    let cell3 = document.createElement("td");
    cell3.textContent = emp.email;
    row.appendChild(cell3);

    let cell4 = document.createElement("td");
    cell4.textContent = emp.gender;
    row.appendChild(cell4);

    // Add the row to the tbody
    tbody.appendChild(row);
});
