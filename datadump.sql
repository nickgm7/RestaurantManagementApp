--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: chef; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.chef (
    chef_id smallint NOT NULL,
    name text,
    salary integer
);


ALTER TABLE public.chef OWNER TO chuckles;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.customer (
    customer_id smallint NOT NULL,
    name text,
    address text,
    phone_num text
);


ALTER TABLE public.customer OWNER TO chuckles;

--
-- Name: dish; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.dish (
    dish_id smallint NOT NULL,
    name text,
    description text,
    price real
);


ALTER TABLE public.dish OWNER TO chuckles;

--
-- Name: ingredient; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.ingredient (
    ingredient_id smallint NOT NULL,
    name text,
    inventory smallint
);


ALTER TABLE public.ingredient OWNER TO chuckles;

--
-- Name: manager; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.manager (
    manager_id smallint NOT NULL,
    name text,
    salary real
);


ALTER TABLE public.manager OWNER TO chuckles;

--
-- Name: order; Type: TABLE; Schema: public; Owner: cam
--

CREATE TABLE public."order" (
    customer_id integer NOT NULL,
    dish_id integer
);


ALTER TABLE public."order" OWNER TO cam;

--
-- Name: order_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: cam
--

CREATE SEQUENCE public.order_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_customer_id_seq OWNER TO cam;

--
-- Name: order_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cam
--

ALTER SEQUENCE public.order_customer_id_seq OWNED BY public."order".customer_id;


--
-- Name: supplier; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.supplier (
    supplier_id smallint NOT NULL,
    name text,
    city text,
    phone_num text
);


ALTER TABLE public.supplier OWNER TO chuckles;

--
-- Name: waiter; Type: TABLE; Schema: public; Owner: chuckles
--

CREATE TABLE public.waiter (
    waiter_id smallint NOT NULL,
    name text,
    salary integer
);


ALTER TABLE public.waiter OWNER TO chuckles;

--
-- Name: order customer_id; Type: DEFAULT; Schema: public; Owner: cam
--

ALTER TABLE ONLY public."order" ALTER COLUMN customer_id SET DEFAULT nextval('public.order_customer_id_seq'::regclass);


--
-- Data for Name: chef; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.chef (chef_id, name, salary) FROM stdin;
178	Nita Johnston	66412
450	Julia Bradford	65579
151	Riley Davidson	40620
467	Pauline Crane	71633
387	Lorrie Guzman	72287
124	Norberto Frederick	52546
137	Sal Levy	46722
216	Reinaldo Valdez	59425
241	Sharron Middleton	44294
370	Regina Mullen	49342
220	Polly Aguirre	70758
170	Lacy Stout	46746
207	Enid Reeves	72606
365	Jerold Gates	71638
283	Lazaro Hood	73076
390	Joesph Leblanc	65944
183	Zackary Anderson	55373
313	Maude Duke	57700
419	Shayne Richards	48543
350	Emmett Cooke	63131
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.customer (customer_id, name, address, phone_num) FROM stdin;
187	Shelby Mcdougall	86909 Cruickshank Harbor, Suite 318, 66669, Turcottechester, Indiana, United States	(309) 721-9910
157	Jaimee Dyer	8629 Kaylah Square, Apt. 562, 39610, Jewelview, Alabama, United States	(915) 908-7512
325	Grace Juarez	78408 Hermiston Spur, Suite 334, 19123, Andrewview, Louisiana, United States	(683) 505-8787
382	Esther Baldwin	71124 Ondricka Creek, Suite 924, 60636, Leschberg, Vermont, United States	(846) 626-5165
209	Shania Herbert	0850 Audra Glens, Suite 507, 15119-7166, Lake Lonnyview, Oregon, United States	(743) 337-3683
365	Tyra Mcbride	5490 Welch Skyway, Suite 474, 66527, North Randalbury, Colorado, United States	(727) 492-5386
245	Xena Mcphee	656 Dicki Island, Suite 635, 03761, New Abelchester, Arizona, United States	(822) 789-4346
183	Nida Reeves	65078 Myrtice Viaduct, Apt. 777, 28066-2132, South Henderson, Hawaii, United States	(360) 940-1696
129	Jeff Mccabe	81387 Jeanne Place, Apt. 128, 06984, Roobside, Rhode Island, United States	(409) 471-8120
387	Noor Doherty	42880 Bradtke Inlet, Suite 021, 59934-4030, Lake Jerrellmouth, Kentucky, United States	(419) 742-0572
177	Chelsy Greig	72252 Quitzon Summit, Suite 247, 94899-8766, Lake Raoul, Texas, United States	(386) 528-4185
317	Owais Driscoll	151 Okuneva Mission, Suite 212, 40525-5523, Koryburgh, Connecticut, United States	(329) 961-0317
407	Latisha Waters	53931 Ayana Tunnel, Suite 969, 95761-3600, East Edgarstad, Kansas, United States	(763) 897-3812
490	Margo Guest	8012 Viva Centers, Suite 456, 66853, North Pablo, Kansas, United States	(522) 383-1615
479	Whitney Mcneill	627 Fae Turnpike, Suite 002, 79983-5967, O'Connerview, Maine, United States	(516) 835-6868
339	Caitlyn Walton	77116 Emard Highway, Suite 265, 86337-1646, Earlenefurt, Alaska, United States	(230) 938-1245
191	Mia-Rose Guevara	4588 Hane Forks, Suite 405, 30084-0823, Lake Dahlialand, Georgia, United States	(865) 653-1901
107	Bryony Contreras	11893 Carter Coves, Apt. 108, 96680-5642, Catherinemouth, Tennessee, United States	(933) 872-1670
385	Roxie Rawlings	36294 Myra Ramp, Suite 221, 38847, North Lexusberg, New York, United States	(246) 559-3208
287	Bradley Davey	3804 Mayer Villages, Apt. 643, 86712-8359, Prosaccoborough, Missouri, United States	(766) 270-0670
45	Adam ludwig	fairy tell lane	322 -654- 4932
3242	53	sasf3242	345352
\.


--
-- Data for Name: dish; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.dish (dish_id, name, description, price) FROM stdin;
108	Lemon and bacon cupcakes	Moist cupcakes made with tangy lemon and lea bacon	11.53
121	Okra and shallot stir fry	Crunchy stir fry featuring fresh okra and shallot	19.61
123	Chicken and egg spaghetti	Spagetti topped with a blend of free range chicken and eggs	18.1
125	Socca and chorizo salad	Socca and Spanish chorizo served on a bed of lettuce	19.59
135	Salmon and chocolate crepes	Fluffy crepes filled with smoked salmon and plain chocolate	21.47
138	Lamb and olive fusilli	Fresh egg pasta in a sauce made from succulent lamb and olive	23.66
151	Jaggery and pepper salad	A crisp salad featuring jaggery and fresh pepper	14.27
160	Mortadella and chocolate mousse	A creamy mousse made with mortadella and white chocolate	11.1
166	Almond and banana biscuits	Crunchy biscuits made with chopped almond and fresh banana	17.59
167	Cannellini and artichoke soup	Dried cannellini and fresh artichoke combined into creamy soup	13.91
172	Milk chocolate and sultana cookies	Crumbly cookies made with milk chocolate and sultana	14.03
180	Vacherin and red onion salad	A crunchy salad featuring vacherin and dried red onion	14.71
182	Rabbit and tarragon salad	Rabbit and dried tarragon served on a bed of lettuce	15.82
185	Turkey and shrimp soup	Free-range turkey and shrimp combined into chunky soup	21.45
192	Bean and pesto lasagne	Layers of fresh egg pasta interspersed with bean and basil pesto	16.14
195	Pepper and crayfish bagel	A warm bagel filled with fresh pepper and crayfish	11.55
196	Egg and apple pizza	Deep pan pizza topped with free range eggs and green apple	17.85
201	Ugli fruit and coconut milk salad	Fresh ugli fruit and coconut milk served on a bed of lettuce	13.36
202	Date and mandarin salad	Moist date and mandarin served on a bed of lettuce	14.26
210	Mackerel and camembert salad	A crunchy salad featuring smoked mackerel and camembert	19.49
\.


--
-- Data for Name: ingredient; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.ingredient (ingredient_id, name, inventory) FROM stdin;
132	pork	15
405	rice vinegar	3
496	mortadella	18
459	rhubarb	3
457	white wine vinegar	13
380	banana	15
308	potatoes	3
445	pumpkin	17
137	tzatziki	10
134	cayenne	17
375	vanilla	20
362	onions	12
499	persimmon	15
305	celery	9
332	ezekiel	13
449	currant	21
334	rambutan	18
364	caper	16
206	bacon	17
124	onion	15
\.


--
-- Data for Name: manager; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.manager (manager_id, name, salary) FROM stdin;
223	Derrick Erickson	51505
409	Belle Whelan	65043
361	Erica Gaines	51708
230	Ari Lambert	53107
125	Mamie Madden	53558
195	Nabila Emerson	74112
359	Laurie Forbes	43586
352	Amalie Ortega	57824
188	Kabir Chandler	48024
472	Cillian Giles	37606
442	Yash Dunn	66343
334	Simrah Cruz	42282
270	Hettie O'Brien	36385
377	Mandeep Fuller	42359
159	Taslima Bowler	36224
437	Leilani Odling	39017
226	Ottilie Pearce	47490
432	Bethanie Rivers	46042
342	Darryl Compton	50631
165	Samira Frye	63994
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: cam
--

COPY public."order" (customer_id, dish_id) FROM stdin;
45	135
3242	108
\.


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.supplier (supplier_id, name, city, phone_num) FROM stdin;
369	Alejandro Bonilla	Glendale	(887) 634-2551
440	Mariyah Hutchinson	New Orleans	(635) 582-6297
165	Murtaza Adamson	Newport News	(649) 967-5559
257	Jamie Gutierrez	Buffalo	(541) 920-9179
479	Suzannah Little	Athens	(792) 955-1464
216	Giorgio Warner	Fullerton	(281) 851-8326
497	Malaki Russell	Concord	(869) 927-3611
473	Ellisha Lake	Torrance	(914) 663-7422
372	Emelie Santiago	Rochester	(767) 567-1193
412	Reuben Whelan	College Station	(496) 992-7911
296	Reginald Werner	Renton	(724) 723-2445
348	Rio Howells	Boulder	(539) 959-4679
131	Oakley Hume	Green Bay	(877) 957-4255
307	Nahla Hoffman	Everett	(524) 302-9756
426	Sarah Kumar	Allentown	(877) 568-4161
462	Cassian Ware	Sandy Springs	(296) 668-5191
457	Ismael Mcgee	Chicago	(784) 673-0365
476	Lucia Leigh	Aurora	(522) 293-2551
350	Ziva Gale	Antioch	(411) 696-4303
278	Charmaine Bolton	Spokane	(218) 748-4557
\.


--
-- Data for Name: waiter; Type: TABLE DATA; Schema: public; Owner: chuckles
--

COPY public.waiter (waiter_id, name, salary) FROM stdin;
235	Louise Trevino	17096
426	Millicent Lambert	14167
273	Michel Johns	21312
388	Belinda Hammond	22838
377	Jon Gonzalez	22713
418	Reginald Robinson	15029
229	Jere Case	22951
451	Krista Lyons	17150
156	Colton Page	19260
169	Jenny Douglas	19864
176	Terrell Vincent	21592
258	Gonzalo Hoover	20152
306	Lenny Keller	17385
398	Brittany Paul	20357
170	Velma Blanchard	16318
135	Basil Goodwin	22535
197	Emma Johnson	17177
482	Timmy Townsend	21302
154	Merle Mayer	19180
370	Lucius Tucker	20727
32	test	31435
4	Jane Smith	54256
\.


--
-- Name: order_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cam
--

SELECT pg_catalog.setval('public.order_customer_id_seq', 1, false);


--
-- Name: chef chef_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.chef
    ADD CONSTRAINT chef_pkey PRIMARY KEY (chef_id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);


--
-- Name: dish dish_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_pkey PRIMARY KEY (dish_id);


--
-- Name: ingredient ingredient_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.ingredient
    ADD CONSTRAINT ingredient_pkey PRIMARY KEY (ingredient_id);


--
-- Name: manager manager_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.manager
    ADD CONSTRAINT manager_pkey PRIMARY KEY (manager_id);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: cam
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (customer_id);


--
-- Name: supplier supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (supplier_id);


--
-- Name: waiter waiter_pkey; Type: CONSTRAINT; Schema: public; Owner: chuckles
--

ALTER TABLE ONLY public.waiter
    ADD CONSTRAINT waiter_pkey PRIMARY KEY (waiter_id);


--
-- PostgreSQL database dump complete
--

