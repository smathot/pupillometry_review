# The pupil light response


## Profile

The pupil light response (PLR), also called the pupil light reflex, is the constriction of the pupil in response to brightness, and the dilation of the pupil in response to darkness. %FigLightResponse shows a typical PLR, elicited by 10 s of blue or red light presented on a computer monitor, followed by 20 s of a dark screen.


%--
figure:
  id: FigLightResponse
  source: lightresponse.svg
  caption: The profile of a typical pupil light response. This figure shows data of myself while I'm looking at red or blue full-screen colors on a computer display. Errors bars reflect the standard error. All data shown in this figure and others is available through the URL provided at the end of the article.
--%


The profile of a typical PLR looks as follows:

- [Light on] 0 - 0.2s: This is the latency period during which the pupil does not yet respond. The exact latency depends on many factors, such as stimulus intensity (latencies decrease with stimulus intensity) and age (latencies increase with age) [@Ellis1981].
- [Light on] 0.2 - 1.5 s: The pupil constricts strongly and rapidly until it reaches its minimum size.
- [Light on] 1.5 - 10 s: The pupil either remains fully constricted while the light remain ons, or unconstricts (redilates) slightly. This unconstriction, when it occurs, is sometimes called *pupil escape*; whether it occurs depends on the color of the light: blue light leads to sustained constriction, whereas red light leads to pupil escape. This difference results from the different photoreceptors that are sensitive to blue and red light, as described below.
- [Light off] 10 s - 30 s: The pupil gradually recovers to its original size. This sometimes called the darkness response, and is much slower than the light response. It can take many seconds for the pupil to fully recover, and recovery is faster for red than blue light, again because of the photoreceptors that are sensitive to red and blue light. After a high-intensity blue light, the pupil remains slightly constricted for many minutes. This is called the post-illumination pupil response (PIPR) [@Markwell2010].


## Neural basis and photoreceptors

The PLR is driven by all known types of photoreceptors: rods, cones, and intrinsically photosensitive retinal ganglion cells (ipRGCs) [@McdougalGamlin2008;@Kardon2005;@Markwell2010].

Cones are sensitive to color, in the sense that there are three types of cones that are maximally responsive to different colors, and the relative activation of these different cone types allows us to distinguish between different colors. (That is, individual cones do not 'see color'.) Cone density is highest in the fovea, and (compared to rods) cones require intense light to become active; therefore, cones dominate central vision, and vision in medium-to-bright levels of light.

Rods are not sensitive to color, in the sense that all rods are maximally sensitive to the same shade of blueish green, and can therefore not distinguish between different colors. Rods are mostly absent from the fovea, and (compared to cones) respond also to weak light; therefore, rods dominate peripheral vision in darkness.

ipRGCs are ganglion cells that receive input from rods and cones, but also contain a photopigment (melanopsin) themselves [@Berson2002]. ipRGCs respond much more slowly to light than rods and cones do. In addition to their role in the PLR, ipRGCs project to the suprachiasmatic nucleus (SCN) of the hypothalamus (sometimes called the biological clock) to maintain the circadian (day-night) rhythm. ipRGCs respond maximally to blueish light [@Markwell2010]. ipRGCs seem to contribute mostly to non-image-forming vision, that is, to visual functions that are not accompanied by conscious visual awareness, such as pupil responses and maintenance of circadian rhythm; however, some studies suggest that ipRGCs may also play a minor role in conscious visual perception [@Ecker2010;@Zaidi2007].

Rods and cones drive the initial pupil constriction of the PLR (0.2 - 1.5 s). This initial constriction therefore has many of the same properties as regular human vision, including that it is strongest for light presented in central vision [@Crawford1936;@Hong2001].

However, input from rods and cones desensitizes quickly; therefore, if the PLR was based only on rod and cone vision, the pupil would rapidly unconstrict even while the light was still on. ipRGCs are the reason why our pupils stay constricted: once rod and cone input reduces, ipRGCs start responding and keep the pupil constricted for as long as the light is on [@Gamlin2007]. %FigLightResponse shows indirect evidence for the role of ipRGCs in maintaining pupillary constriction: Constriction (1.5 - 10 s) is more sustained for blue than red light, because ipRGCs are maximally sensitive to blueish light. ipRGCs also drive the PIPR, which is therefore also strongest for blue light. Simply put: because of rods and cones, the pupil rapidly constricts in response to sudden light increases; but because of ipRGCs, the pupil stays constricted throughout the day [@Wong2012Hours;@Gooley2012].

Signals from rods, cones, and ipRGCs go to the pretectal olivary nucleus (PON), and from there follow the pupillary constriction pathway as shown in %FigPathways::a.


## Cognitive influences


### Visual awareness

Historically, the PLR was considered a purely reflexive response to the amount of light that falls on the retina. However, several elegant studies using binocular rivalry, dating back almost a century, already showed that this is not the full story [@LoweOgle1966;@Brenner1969;@BárányHalldén1948;@Harms1937]+[; for recent replications, see @Fahle2011;@Kimura2014;@Naber2011]+[; for reviews, see @Binda2014Trends;@Math2015CurrDir].

For example, @BárányHalldén1948 presented a horizontal line to one eye, and a vertical line to the other eye. This different visual input to both eyes induced binocular rivalry: participants sometimes consciously perceived the horizontal line, and sometimes the vertical line, but rarely both. In addition, the researchers occasionally flashed a dim light into one of the eyes, and recorded whether this flash triggered a measurable pupil constriction or not. Crucially, they found that a measurable pupil constriction was more likely to be triggered when the light was flashed into the eye that, at that moment, dominated visual awareness. Phrased differently, the PLR was strongest for light sources that were consciously perceived—a clear demonstration of how high-level cognition influences the PLR.


### Covert visual attention

More recently, it has been shown that covert visual attention also modulates the PLR [@Mathôt2013Plos;@Naber2013Osc;@Binda2013Enhances;@BindaMurray2015;@Binda2014Feature;@Mathôt2014JVis;@Bombeke2016;@UnsworthRobison2016;@Ebitz2014]. For example, in one of our own experiments, participants fixated their gaze in the center of a display that was bright on one side, and dark on the other side [@Mathôt2013Plos]. We then presented a cue, either an arrow or a voice saying "left" or "right", that indicated the probable location of an upcoming target. Without moving their eyes, participants shifted their attention to the cued side, which could be either dark or bright. Crucially, we found that pupils were smaller when participants covertly attended to the bright side of the display, compared to the dark side of the display. In other words, covertly attending to something that is bright or dark causes a PLR, just like (although much more weakly than) directly looking at something that is bright or dark. This effect is so robust that it can even be used to decode whether people are covertly attending to something bright or dark, with around 90% accuracy on a single-trial level [@Mathôt2016Plos].

Neurophysiological studies have shown similar effects [@EbitzMoore2017;@WangMunoz2016]. For example, @EbitzMoore2017 stimulated neurons in the frontal eye field (FEF) of the rhesus macaque. The FEF is a brain area in the prefrontal cortex (PFC), and is involved in eye movements and covert shifts of attention: strong (suprathreshold) FEF stimulation  triggers eye movements; weak (subthreshold) stimulation triggers covert shifts of attention. In their study, @EbitzMoore2017 first stimulated FEF neurons to trigger a covert of shift of attention to the receptive field (RF) of these neurons (i.e. the location in the visual field to which these neurons respond); next, they flashed a stimulus either within, or outside of, the stimulated RF. Crucially, they observed a stronger PLR to stimuli flashed within the stimulated RF, compared to outside of the stimulated RF—a result that echoes behavioral studies [notably @BindaMurray2015].


### Eye-movement preparation

When you prepare an eye movement toward an object, but before your eyes actually set in motion, you already begin to perceive the to-be-looked-at object more clearly in your mind's eye; phrased differently, each eye movement is preceded by a covert shift of attention [@DeubelSchneider1996Attention;@Kowler1995;@HoffmanSubramaniam1995]. Given the results discussed above, a natural question is whether this presaccadic shift of attention results in a preparatory pupil light response; that is, when you make an eye movement toward a lamp, does your pupil already begin to constrict before your eyes start to move?

To test this, we conducted an experiment in which participants initially fixated in the center of a display that was divided into a bright and a dark half [@MathôtLinden2015Prep]+[; see also @Ebitz2014]. Next, an auditory cue (a spoken word "left" or "right") instructed participants to make an eye movement toward either the left or the right side of the display, which could be either bright or dark. Crucially, we found that the pupil began to respond (weakly) to the brightness of the cued side already while the eyes were in still motion. Because the minimum latency of the PLR is about 200 ms [@Ellis1981, see also %FigLightResponse], this zero-latency response clearly resulted from preparation, presumably mediated through a presaccadic shift of attention.

That a PLR is prepared along with an eye movement, rather than being a passive consequence of it, makes ecological sense, considering that humans make about three eye movements per second [e.g. @Rayner1998]. Given that it takes at least 200 ms for the pupil to respond to light [@Ellis1981], this would mean that by the time that the pupil start to respond to the brightness of a newly fixated object, gaze has already shifted elsewhere; or at least that's what would happen in the absence of any preparation. By reducing the effective latency of the PLR, preparation may allow the sluggish PLR to keep up with our eye movements.


### Subjective interpretation

Whether a stimulus is subjectively interpreted as being bright (or not) also determines how strongly the pupil responds to it [@Zavagno2017;@LaengEndestad2012;@Bombeke2016;@Binda2013Sun;@Naber2013Content]. For example, @Naber2013Content showed images, either photographs or cartoons, to participants. Crucially, they found that images that contained a sun triggered stronger pupil constriction than images that did not contain a sun, even when eye position and objective luminance were controlled for. This effect disappeared when images were flipped vertically, presumably because vertically flipped images are difficult to interpret.

From this finding, the authors concluded that the PLR reflects subjective interpretation: an image that we interpret as being very bright (such as an image of the sun) causes a strong pupil constriction, even when the objective luminance of the image is modest.


### Mental imagery and word meaning

In the studies described above, pupil responses were always triggered by visual stimuli (even though the strength of the pupil response was modulated by cognitive influences). However, several studies suggest that the pupil may even constrict in response to mental images, that is, in response to an internally generated image without actual visual input [@LaengSulutvedt2014;@Mathôt2017Words].

In one experiment, @LaengSulutvedt2014 asked participants to look at a uniformly gray screen, while mentally picturing that they were in a particular environment. Crucially, @LaengSulutvedt2014 found that participants' pupils constricted when they mentally pictured being in a bright, compared to a dark, environment; that is, the pupil was smaller when participants imagined themselves outdoors under a sunny sky, compared to indoors in a dark room.

In a series of our own experiments, participants read or heard individual words [@Mathôt2017Words]. To make sure that participants processed the meaning of the words, they were instructed to press spacebar whenever the word was an animal name. Some of the non-animal words were associated with brightness (e.g. 'sun'); others were associated with darkness (e.g. 'night'). Crucially, we found that participants' pupils were smaller when they read or heard words that conveyed a sense of brightness, compared to words that conveyed a sense of darkness. Echoing the study of @LaengSulutvedt2014, we interpreted this in terms of mental imagery: when participants read a word, they automatically simulate the perceptual properties of the word's referent [e.g. @Pulvermüller2013]+[; but see @MahonCaramazza2008 for a different perspective]; for example, when participants read 'sun', they automatically create a mental image of a bright ball of fire in the sky. And, plausibly, this mental image then causes the pupil to constrict.


### Working memory

When discussing the PLR in the context of visual working memory, it is important to clearly distinguish this from the classic studies of @KahnemanBeatty1966 and others. @KahnemanBeatty1966 have shown that the pupil dilates when you keep items in working memory; this is an effect of mental effort, which we will get back to in the section on the psychosensory pupil response. In contrast, the studies described in this section address a different question: Can we tell *what* someone keeps in memory by looking at pupil size? More specifically, can we use the PLR to track whether someone keeps something bright or something dark in working memory?

In one of our experiments, participants memorized a location, which could be either on a dark or a bright background [@Fabius2017Pupil; see also @UnsworthRobison2016]. We found that the pupil was smaller when participants memorized a location on a bright, compared to a dark, background. This suggests that memorizing a location is similar to covertly attending to a location, in line with previous research [e.g. @AwhJonides1998Rehearsal]. However, in this study, the bright/ dark background was continuously visible; therefore, the effect was not necessarily (and was probably not) driven by a memory representation of brightness or darkness per se, but rather by a more-or-less sustained shift of attention to the bright or dark background.

To test whether a memory representation of brightness or darkness also triggers a PLR, we conducted another series of experiments in which we asked participants to memorize either bright or dark stimuli [@Blom2016]; that is, rather than asking participants to memorize a location on a continuously visible bright or dark background, we asked participants to memorize bright or dark objects that were subsequently removed from the display. Crucially, we found no evidence that, after the stimuli had been removed from the display, maintaining bright or dark stimuli in working memory affected pupil size.

Given the studies described in the previous section (Mental imagery and word meaning), which showed that pupil size is affected by a mental image of brightness or darkness [@LaengSulutvedt2014], the finding that pupil size is *not* affected by keeping bright or dark objects in working memory is surprising: Surely visual working memory is closely related to mental imagery? Future studies may shed light on this apparent discrepancy.


## Function

How does the PLR help visual perception? This seemingly obvious question does not have a clear-cut answer, and even experts often provide different, though not mutually exclusive, answers [@WoodhouseCampbell1975]. But several functions are generally assumed to play a role [reviewed in @Math2015CurrDir].

The benefit of a dilated pupil is clear: A large pupil lets a lot of light into the eye, thus increasing the amount of visual information that the brain receives, thus increasing visual sensitivity; therefore, a dilated pupil, compared to a constricted pupil, allows you to better detect faint stimuli. Imagine a cat in the dark, looking for small moving stimuli (mice); this cat would probably benefit from large pupils that capture as much light as possible. The question thus becomes why the pupil is not always maximally dilated. Why don't the eyes always capture as much light as they can?

First, a mobile pupil acts as a buffer when transitioning from brightness to darkness [@Barlow1972;@WoodhouseCampbell1975]. When you are in brightness, rods and cones are light adapted ('bleached'), which makes them less sensitive to light. When you then go from brightness into darkness, rods and cones need to adapt. Dark adaptation is a gradual process that, especially for rods, takes tens of minutes. During the period that you are in darkness while dark adapation is not yet complete, vision is impaired. Because the pupil can dilate much more rapidly than rods and cones can adapt, pupil dilation reduces the amount of dark adaptation that is necessary, thus (compared to a static pupil) improving vision during the first few minutes of dark adaptation. (Light adaptation is a very rapid process, and does not appear to benefit as much, or at all, from the PLR.)

Second, pupil constriction increases depth of field: the range of distances at which vision is sharp [@Campbell1957;@CharmanWhitefoot1977]. This is because a constricted pupil exposes only a small part of the eye's lens, and a small lens, compared to a large lens, suffers less from optical distortions that reduce depth of field. While focusing on a point that is very far away, a fully constricted pupil (± 2 mm diameter) provides sharp vision from about 2 m distance to infinity, whereas a fully dilated pupil (± 8 mm diameter) provides sharp vision from about 7 m distance to infinity. Therefore, to the extent that a large depth of field is advantageous, a constricted pupil is advantageous as well.

Third, pupil constriction increases visual acuity: how well you can discriminate fine detail [@CampbellGregory1960;@Woodhouse1975Detection;@LiangWilliams1997]. Analogous to depth of field, this is because a constricted pupil, and thus a small lens, suffers less from optical distortions (spherical and chromatic abberations) that cause optical blur. @Woodhouse1975Detection estimated that a constricted pupil, compared to a dilated pupil, improves visual acuity by about 20% under conditions of high luminance. When the pupil becomes too small, a different set of optical distortions (diffractions) emerge that impair, rather than improve, visual acuity; this may be why the minimum size of the human pupil is about 2 mm, just above the size at which these distortions come into play.

The PLR thus likely helps vision by reducing dark adaption, and by optimizing the trade-off between visual acuity and depth of field (which benefit from a small pupil) and visual sensitivity (which benefits from a large pupil, especially in darkness). But, in humans, these effects are small, and vision would likely not be strongly impaired if the pupil would not respond to light. (Although this is difficult to prove, because there seems to be no naturally occurring condition in which pupil size is fixed while vision is otherwise healthy.) However, other animals have far larger ranges of pupil sizes than humans, and thus may benefit more from the PLR. For example, the area of the slit pupil of the Gecko can change by a factor of 300 [@Denton1956].

And, even if the PLR confers but little advantage, "one should bear in mind that seemingly trivial advantages may become extremely significant in a competitive situation; thus an animal whose pupil can dilate a little more may acquire a distinct competitive edge at dusk, and this could make the difference between starvation and plenty." [@Barlow1972, p.3]
