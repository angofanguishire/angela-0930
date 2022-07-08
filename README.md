## Named Entity Recognition (NER) Playground
A simple NER interface that allows users to input some English text and process it to display corresponding entity tags.

### Installation
Open a terminal and copy or clone the repository. Move into the directory __angela-0930__ with `cd angela-0930`. It is required that docker and docker compose are installed in your machine in advance. Run `docker-compose up` as a command. Open your favorite web browser and go to `http://127.0.0.1:10101/demo`.

### Usage
The web interface consists of a text input field, a submit button, and an output area for the NER processed text tagged with its entities that looks like the following:

![Screenshot from 2022-07-08 02-52-11](https://user-images.githubusercontent.com/73561768/177967307-44b34534-8411-4f64-8aa7-7ac717d8a7eb.png)

If we enter the following snippet,
> The design of the Eiffel Tower is attributed to Maurice Koechlin and Émile Nouguier, two senior engineers working for the Compagnie des Établissements Eiffel. It was envisioned after discussion about a suitable centerpiece for the proposed 1889 Exposition Universelle, a world’s fair to celebrate the centennial of the French Revolution. Eiffel openly acknowledged that inspiration for a tower came from the Latting Observatory built in New York City in 1853. In May 1884, working at home, Koechlin made a sketch of their idea, described by him as “a great pylon, consisting of four lattice girders standing apart at the base and coming together at the top, joined together by metal trusses at regular intervals”. Eiffel initially showed little enthusiasm, but he did approve further study, and the two engineers then asked Stephen Sauvestre, the head of the company’s architectural department, to contribute to the design. Sauvestre added decorative arches to the base of the tower, a glass pavilion to the first level, and other embellishments. (https://en.wikipedia.org/wiki/Eiffel_Tower)

we obtain the following result:
> The design of the Eiffel Tower is attributed to Maurice \[Koechlin\](ORG) and Émile Nouguier, \[two\](CARDINAL) senior engineers working for the Compagnie des Établissements Eiffel. It was envisioned after discussion about a suitable centerpiece for the proposed \[1889\](DATE) Exposition Universelle, a world’s fair to celebrate the centennial of the French Revolution. Eiffel openly acknowledged that inspiration for a tower came from the Latting Observatory built in New York City in 1853.In May 1884, working at home, \[Koechlin\](ORG) made a sketch of their idea, described by him as “a great pylon, consisting of \[four\](CARDINAL) lattice girders standing apart at the base and coming together at the top, joined together by metal trusses at regular intervals”. Eiffel initially showed little enthusiasm, but he did approve further study, and the \[two\](CARDINAL) engineers then asked Stephen Sauvestre, the head of the company’s architectural department, to contribute to the design. \[Sauvestre\](PERSON) added decorative arches to the base of the tower, a glass pavilion to the \[first\](ORDINAL) level, and other embellishments.

You can always clear the results by pressing the `Try again` button and run tests on other text snippets.

### Troubleshooting
If it is necessary to restart the terminal and redeploy the docker containers, be sure to remove the docker containers first. In the terminal, we can run
```
user@user:~/angela-0930$ docker stop frontend_container backend
user@user:~/angela-0930$ docker rm frontend_container backend
user@user:~/angela-0930$ docker-compose up 
```
