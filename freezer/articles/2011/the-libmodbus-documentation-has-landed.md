title: The libmodbus documentation has landed
published: 2011-03-25
tags: [libmodbus, gnome]

You've been numerous to ask for documentation and the work of
[gass](https://github.com/gass) with GTK-doc help me to prioritize it, so this
month I've finally tackled this problem but not as expected!

At first, I loved the GTK-doc solution, I'm a GNOME lover after all, but GTK-doc
can't generate man pages and the setup code is too cumbersome IMHO. To choose
the best solution for [libmodbus][], I read a comparison matrix on Wikipedia,
after some tests with GTK-doc, Doxygen and AsciiDoc, and I finally choose
AsciiDoc.

However, there is a major difference between AsciiDoc and the other envisaged
solutions, the documentation isn't included in the source code. I used to think
it was good idea to keep the both at the same place to keep them in sync but:

- it doesn't prevent you to code without updating the documentation
- the documentation must be escaped by the language comment tags
- I don't want to abuse my wheel mouse (to skip documentation) when I
  code

The 0MQ project, endless source of inspiration, was a very good starting point
to learn some tricks with AsciiDoc.

Now, I'm looking for help to review and extend the documentation which has just
landed in git (`make doc` to generate man pages). I've generated the
[documentation in HTML][doc] for the web site.

[libmodbus]: http://libmodbus.org/
[doc]: http://libmodbus.org/documentation
