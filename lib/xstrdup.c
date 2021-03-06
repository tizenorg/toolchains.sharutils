/* xstrdup.c -- copy a string with out of memory checking
   Copyright (C) 1990, 1996, 1998, 2001, 2007 Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.  */

#if HAVE_CONFIG_H
# include <config.h>
#endif

#if STDC_HEADERS || HAVE_STRING_H
# include <string.h>
#else
# include <strings.h>
#endif

#include <sys/types.h>

#include "xalloc.h"

/* Return a newly allocated copy of STRING.  */

char *
xstrdup (const char *string)
{
  return strcpy (xmalloc (strlen (string) + 1), string);
}
