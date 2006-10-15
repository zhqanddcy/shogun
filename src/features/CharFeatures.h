/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * Written (W) 1999-2006 Soeren Sonnenburg
 * Copyright (C) 1999-2006 Fraunhofer Institute FIRST and Max-Planck-Society
 */

#ifndef _CHARFEATURES__H__
#define _CHARFEATURES__H__

#include "features/SimpleFeatures.h"
#include "features/Alphabet.h"
#include "lib/common.h"

class CCharFeatures: public CSimpleFeatures<CHAR>
{
	public:
		CCharFeatures(E_ALPHABET, INT size);
		CCharFeatures(CAlphabet* alpha, INT size);
		CCharFeatures(const CCharFeatures & orig);
        CCharFeatures(E_ALPHABET alphabet, CHAR* feature_matrix, INT num_feat, INT num_vec);
		CCharFeatures(E_ALPHABET alphabet, CHAR* fname);

		~CCharFeatures();

		inline CAlphabet* get_alphabet()
		{
			return alphabet;
		}

		virtual bool load(CHAR* fname);
		virtual bool save(CHAR* fname);
	protected:
		CAlphabet* alphabet;
};
#endif
