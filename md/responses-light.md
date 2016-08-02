# The pupil light response


## Profile

The pupil light response (PLR), also called the pupil light reflex, is the constriction of the pupil in response to brightness, and the dilation of the pupil in response to darkness. %FigLightResponse shows a typical PLR, elicited by 10 s of light presented on a computer monitor, followed by 10 s of darkness.


%--
figure:
  id: FigLightResponse
  source: lightresponse.svg
  caption: The profile of a typical pupillary light response.
--%


The profile of a typical PLR looks as follows:

- Light on:
	- 0 - 0.2s : This is the latency period during which the pupil does not yet respond.
	- 0.2 - 1.5 s: The pupil constricts strongly and rapidly until it reaches its minimum size.
	- 1.5 - 10 s: The pupil either remains fully constricted while the light is on, or unconstricts slightly. This unconstriction, when it occurs, is sometimes called pupillary escape; whether it occurs depends on the color of the light: blue light leads to sunstained constriction, whereas red light leads to pupillary escape. This difference results from the different photoreceptors that are sensitive to blue and red light, as described below.
- Light off:
	- 10 s - 30 s: The pupil gradually recovers to its original size. This sometimes called the darkness response, and is much slower than the light response. It can take many seconds for the pupil to fully recover, and recovery is faster for red than blue light, again because of the photoreceptors that are sensitive to red and blue light. After a high-intensity blue light, the pupil remains slightly constricted for many minutes. This is called the post-illumination pupillary light response (piPLR).


## Photoreceptors and neural basis

The PLR is driven by all photoreceptor classes: rods, cones, and intrinsically photosensitive retinal ganglion cells (ipRGCs) [@McDougalGamlin2005;@Kardon2005].

Cones are color-sensitive, in the sense that there are three types of cones that are maximally responsive to different colors, and the relative activation of these different cones allows us to distinguish between different colors. Cones are mostly found in the fovea, and (compared to rods) require intense light to become activate; therefore, cones dominate central vision, and vision in medium-to-bright levels of light.

Rods are not color-sensitive, in the sense that all rods are maximally sensitive to the same color (blueish), and cannot therefore not to distinguish between different colors. Rods are mostly absent from the fovea, and (compared to cones) respond also to weak light; therefore, rods dominate peripheral vision, and vision in darkness.

ipRGCs are ganglion cells that receive input from rods and cones, but also contain a photopigment (melanopsin) themselves [@Berson2002]. iPRGCs respond much more slowly to light than rods and cones. In addition to their role in the PLR, ipRGCs project to the suprachiasmatic nucleus (SCN) of the hypothalamus--sometimes called the biological clock--to maintain our sense of day and night.

Rods and cones drive the initial pupillary constriction of the PLR (0.2 - 1.5 s). This initial constriction therefore has many of the same properties as regular human vision, including that it is strongest for light presented in central vision [@Crawford1936;@Hong2001].

However, input from rods and cones desensitizes quickly [REF]; therefore, if the PLR was based only on rod and cone vision, the pupil would rapidly redilate even while the light was still on. But this doesn't happen because of ipRGCs: Once rod and cone input disappears, ipRGCs start responding and keep the pupil constricted for as long as the light is on [@Gamlin2007]. %FigLightResponse shows indirect evidence for the role of ipRGCs in maintaining pupillary constriction: Constriction (1.5 - 10 s) is more sustained for blue than red light, because ipRGCs are mostly sensitive to blue light. ipRGCs also drive the piPLR, which is therefore also strongest for blue light. Simply put, because of rods and cones, the pupil rapidly constricts in response to sudden light increases; but because of ipRGCs, the pupil stays constricted throughout the day [@Wong2012hours].

Signals from rods, cones, and ipRGCs go to the pretectal olivary nucleus (PON), and from there follow the pupillary constriction pathway as shown in %FigPathways::a.


## Function

How does the PLR help visual perception? This seemingly obvious question does not have a clear-cut answer, but several functions are generally accepted to play a role [@MathôtVanderstigchel2015].

The benefit of a dilated pupil is clear: A large pupil lets a lot of light into the eye, thus increasing the amount of visual information that the eyes receive, thus increasing visual sensitivity; therefore, a dilated pupil, compared to a constricted pupil, allows you to better detect faint stimuli. The question thus becomes why the pupil is not always maximally dilated. Why don't the eyes always capture as much light as they can?

First, a mobile pupil acts as a buffer when transitioning from brightness to darkness [@Barlow1972;@WoodhouseCampbell1975]. When you are in brightness, rods and cones are light adapted ('bleached'), which makes them less sensitive to light. When you transition from brightness to darkness, rods and cones need to dark adapt. Dark adaptation is a gradual process that, especially for rods, takes tens of minutes. During the period that you are in darkness, but dark adapation is not yet complete, vision is impaired. Because the pupil can dilate much more rapidly than rods and cones can adapt, pupillary dilation reduces the amount of dark adaptation that is necessary, thus (compared to a static pupil) improving vision during the first few minutes of dark adaptation. (The converse, light adaptation is a very rapid process, and does not appear to benefit as much, or at all, from the PLR.)

Second, pupil constriction increases depth of field: the range of distances at which vision is sharp [@Campbell1957;@CharmanWhitefield1977]. This is because a constricted pupil exposes only a small part of the eye's lens, and a small lens, compared to a large lens, suffers less from optical distortions that reduce depth of field. While focusing on a point that is very far away, a fully constricted pupil (± 2 mm diameter) provides sharp vision from about 2 m distance to infinity, whereas a fully dilated pupil (± 8 mm diameter) provides sharp vision from about 7 m distance to infinity. To the extent that a large depth of field is advantageous, a constricted pupil is thus advantageous as well.

Third, pupil constriction increases visual acuity: how well you can discriminate fine detail [@CampbellGregory1960;@Woodhouse1975Detection;@LiangWilliams1997]. Analogous to depth of field, this is because a constricted pupil, and thus a small lens, suffers less from optical distortions (spherical and chromatic abberations) that cause optical blur. @Woodhouse1975Detection estimated that a constricted pupil, compared to a dilated pupil, improves visual acuity by about 20% under conditions of high luminance. When the pupil becomes too small, a different set of optical distortions (diffractions) emerge that impair, rather than improve, visual acuity [REF]; this may be why the minimum size of the human pupil is about 2 mm, just above the size at which these distortions come into play.

The PLR thus helps vision through by reducing dark adaption, and by optimizing the trade-off between visual acuity and depth of field (which benefit from a small pupil) and visual sensitivity (which benefits from a large pupil, especially in darkness). But, in humans, these effects are small, and vision would likely not be strongly impaired if the PLR were absent. (Although this is difficult to prove, because there seems to be no condition in which pupil size is fixed but vision is otherwise healthy.) However, other animals have far larger ranges of pupil sizes than humans, and thus may benefit more from the PLR. For example, the area of the slit pupil of the Gecko can change by a factor of 300 [@Denton1956].

And, even if the PLR confers but little advantage, "one should bear in mind that seemingly trivial advantages may become extremely significant in a competitive situation; thus an animal whose pupil can dilate a little more may acquire a distinct competitive edge at dusk, and this could make the difference between starvation and plenty." [@Barlow1972, p.3]


## Cognitive influences

TODO
