#pragma once
#include "libconfig.h"


struct EXPORT_SYMBOL rgbai{
    struct {
        float r,g,b,a;
    };
    int i;
};

struct EXPORT_SYMBOL color{
    union{
        struct {
            float r,g,b,a;
        };
        float val[4];
    };
};

struct {
    int x;
} unnamed_struct_with_mem_var_x;

typedef struct
{
  rgbai m_rgbai;	  
  union {
    void *vtable;         /* Pointer to function pointers structure.  */
  } ptr_vtable;
} some_struct;

void EXPORT_SYMBOL do_smth2( some_struct* );

void EXPORT_SYMBOL do_smth( color );

